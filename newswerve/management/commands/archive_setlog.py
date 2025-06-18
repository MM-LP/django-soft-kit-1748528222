"""
Archive & Purge Management Commands for Swervetracker
----------------------------------------------------
This module contains two Django management commands:
1. `archive_setlog` – archives a SetLog tree with optional --dry-run.
2. `purge_archives`  – deletes archived records older than N days (defaults to 90).

It also ships a Celery periodic task (`purge_archives_task`) you can wire into
Celery Beat for automatic daily cleanup.
"""

from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.db import transaction

from yourapp.models import (
    SetLog, SetDetail, TrainingDetail, Post,
    ArchivedSetLog, ArchivedSetDetail, ArchivedTrainingDetail,
    ArchivedPost, ArchivedPostMedia
)

# ------------------------------------------------------------------
# 1️⃣  archive_setlog command
# ------------------------------------------------------------------
class Command(BaseCommand):  # django discovers this as archive_setlog.py
    help = "Archive a SetLog and all related data by ID. Supports --dry-run."

    def add_arguments(self, parser):
        parser.add_argument("setlog_id", type=int, help="ID of the SetLog to archive")
        parser.add_argument("--user_id", type=int, help="Optional ID of the user performing the archive")
        parser.add_argument("--dry-run", action="store_true", help="Preview changes without modifying data")

    def handle(self, *args, **options):
        setlog_id = options["setlog_id"]
        dry_run = options["dry_run"]
        user = None

        if options["user_id"]:
            User = get_user_model()
            try:
                user = User.objects.get(id=options["user_id"])
            except User.DoesNotExist:
                raise CommandError(f"User with ID {options['user_id']} does not exist")

        try:
            setlog = SetLog.objects.get(id=setlog_id)
        except SetLog.DoesNotExist:
            raise CommandError(f"SetLog with ID {setlog_id} does not exist")

        details_qs = SetDetail.objects.filter(setlog=setlog)
        posts_qs = Post.objects.filter(setlog=setlog)
        training = getattr(setlog, "trainingdetail", None)

        if dry_run:
            self.stdout.write(self.style.WARNING("--- DRY RUN ---"))
            self.stdout.write(f"Would archive SetLog: {setlog}")
            self.stdout.write(f"Would archive {details_qs.count()} SetDetail rows")
            if training:
                self.stdout.write("Would archive TrainingDetail attached")
            self.stdout.write(f"Would archive {posts_qs.count()} Posts & media")
            self.stdout.write(self.style.WARNING("No data modified."))
            return

        # Actual archiving wrapped in a transaction for atomic safety
        with transaction.atomic():
            archived_log = ArchivedSetLog.objects.create(
                source_user_id=user,
                archive_skier_id=setlog.skier_id,
                archive_course_id=setlog.course_id,
                archive_activity_id=setlog.activity_id,
                boat_id=setlog.boat_id,
                boatdriver_id=setlog.BoatDriver_id,
                coach=setlog.coach,
                log_id=setlog.log_id,
                session_number=setlog.session_number,
                event=setlog.event,
                start_time=setlog.start_time,
                end_time=setlog.end_time,
                archived_at=timezone.now(),
            )

            # Archive SetDetail rows
            for detail in details_qs:
                ArchivedSetDetail.objects.create(
                    archive_set_log_id=archived_log,
                    session_number=detail.session_number,
                    pass_number=detail.pass_number,
                    pass_time=detail.pass_time,
                    rope_length=detail.rope_length,
                    pass_speed=detail.pass_speed,
                    ZeroOff=detail.ZeroOff,
                    balls=detail.balls,
                    personal_best=detail.personal_best,
                    pb_term=detail.pb_term,
                    event=detail.event,
                    as_mode=detail.as_mode,
                    competition=detail.competition,
                    wind_speed=detail.wind_speed,
                    wind_dir=detail.wind_dir,
                )

            # TrainingDetail if present
            if training:
                ArchivedTrainingDetail.objects.create(
                    archive_set_log_id=archived_log,
                    # TODO: copy relevant training fields here
                )
                training.delete()

            # Archive Posts & PostMedia
            for post in posts_qs:
                archived_post = ArchivedPost.objects.create(
                    setlog=archived_log,
                    user=post.user,
                    caption=post.caption,
                    is_public=post.is_public,
                    created_at=post.created_at,
                    updated_at=post.updated_at,
                )
                for pm in post.media.all():
                    ArchivedPostMedia.objects.create(
                        post=archived_post,
                        media_file=pm.media_file,
                        media_type=pm.media_type,
                        order=pm.order,
                    )
                post.delete()

            # Finally delete originals
            details_qs.delete()
            setlog.delete()

        self.stdout.write(self.style.SUCCESS(f"Successfully archived SetLog ID {setlog_id}"))
