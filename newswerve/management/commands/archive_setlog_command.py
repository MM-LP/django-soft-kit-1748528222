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


# ------------------------------------------------------------------
# 2️⃣  purge_archives command (defaults to 90 days)
# ------------------------------------------------------------------
class PurgeArchivesCommand(BaseCommand):  # filename should be purge_archives.py
    help = "Purge archived records older than N days (default 90)."

    def add_arguments(self, parser):
        parser.add_argument("--days", type=int, default=90, help="Age threshold in days")
        parser.add_argument("--dry-run", action="store_true", help="Preview how many rows would be deleted")

    def handle(self, *args, **options):
        days = options["days"]
        dry_run = options["dry_run"]
        cutoff = timezone.now() - timezone.timedelta(days=days)

        qs_log = ArchivedSetLog.objects.filter(archived_at__lt=cutoff)
        qs_detail = ArchivedSetDetail.objects.filter(archive_set_log_id__archived_at__lt=cutoff)
        qs_train = ArchivedTrainingDetail.objects.filter(archive_set_log_id__archived_at__lt=cutoff)
        qs_post = ArchivedPost.objects.filter(setlog__archived_at__lt=cutoff)
        qs_post_media = ArchivedPostMedia.objects.filter(post__setlog__archived_at__lt=cutoff)

        if dry_run:
            self.stdout.write(self.style.WARNING("--- DRY RUN ---"))
            self.stdout.write(f"Would delete {qs_log.count()} ArchivedSetLog rows")
            self.stdout.write(f"Would delete {qs_detail.count()} ArchivedSetDetail rows")
            self.stdout.write(f"Would delete {qs_train.count()} ArchivedTrainingDetail rows")
            self.stdout.write(f"Would delete {qs_post.count()} ArchivedPost rows")
            self.stdout.write(f"Would delete {qs_post_media.count()} ArchivedPostMedia rows")
            self.stdout.write(self.style.WARNING("No data modified."))
            return

        deleted_counts = {
            "ArchivedSetLog": qs_log.delete()[0],
            "ArchivedSetDetail": qs_detail.delete()[0],
            "ArchivedTrainingDetail": qs_train.delete()[0],
            "ArchivedPost": qs_post.delete()[0],
            "ArchivedPostMedia": qs_post_media.delete()[0],
        }

        for model, count in deleted_counts.items():
            self.stdout.write(f"Deleted {count} rows from {model}")

        self.stdout.write(self.style.SUCCESS(f"Purged archives older than {days} days"))


# ------------------------------------------------------------------
# 3️⃣  Celery periodic task for automatic purge
# ------------------------------------------------------------------
from celery import shared_task

@shared_task
def purge_archives_task(days: int = 90):
    """Celery task to purge archived rows older than `days`."""
    cutoff = timezone.now() - timezone.timedelta(days=days)
    ArchivedPostMedia.objects.filter(post__setlog__archived_at__lt=cutoff).delete()
    ArchivedPost.objects.filter(setlog__archived_at__lt=cutoff).delete()
    ArchivedTrainingDetail.objects.filter(archive_set_log_id__archived_at__lt=cutoff).delete()
    ArchivedSetDetail.objects.filter(archive_set_log_id__archived_at__lt=cutoff).delete()
    ArchivedSetLog.objects.filter(archived_at__lt=cutoff).delete()

# In settings.py (Celery Beat) add:
# from celery.schedules import crontab
# CELERY_BEAT_SCHEDULE = {
#     "purge_old_archives": {
#         "task": "yourapp.management.commands.archive_setlog.purge_archives_task",
#         "schedule": crontab(hour=3, minute=0),  # runs daily at 03:00
#         "args": (90,),
#     },
# }
