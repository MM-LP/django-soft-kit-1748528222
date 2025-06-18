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
