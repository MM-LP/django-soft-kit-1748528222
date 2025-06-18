from django.db import models
from .ArchivedTrainingDetail import ArchivedTrainingDetail
from .ArchivedSetLog import ArchivedSetLog
from django.contrib.auth.models import User

class ArchivedSetDetail(models.Model):    
    source_user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)                                          #detailed data for each pass
    archive_set_log_id = models.ForeignKey(ArchivedSetLog, on_delete=models.PROTECT)
    session_number = models.IntegerField(blank=True, null=True)
    pass_number = models.IntegerField(blank=True, null=True)
    pass_time = models.DateTimeField(auto_now=True, null=True)
    rope_length = models.IntegerField(blank=True, null=True)
    pass_speed = models.IntegerField(blank=True, null=True)
    ZeroOff = models.IntegerField(blank=True, null=True)
    balls = models.IntegerField(blank=True, null=True)                      # flag for personal best
    personal_best = models.BooleanField(default=False)
    pb_term = models.CharField(max_length=255, blank=True, null=True)       # Life PB or Annual (year-to-date)
    event = models.CharField(max_length=255, blank=True, null=True)         # slalom, trick, jump (may be redundant)
    as_mode = models.BooleanField(blank=False)                              #used autosteer mode  y/n
    tournament = models.IntegerField(null=True, blank=True)                #id of competition (from competition db - future dev)
    archive_training_id = models.ForeignKey(ArchivedTrainingDetail, on_delete=models.SET_NULL, null=True)  #if not null, connected to a training pgm (training detail table)
    wind_speed = models.IntegerField(null=True, blank=True)                 #get data from SetLog windrss provider
    wind_dir = models.CharField(max_length=5, blank=True, null=True)        # as above  
    wind_rtp = models.CharField(max_length=5, blank=True, null=True)         #wind direction relative to course direction and ski pass

    # surepath_id                                                           # connects to surepath file for this path (future dev)
    # autosteer_id                                                          # connects to autosteer file(s)
                                                            # connect to audio files
    archived_at = models.DateTimeField(auto_now_add=True)