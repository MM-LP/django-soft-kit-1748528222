from django.db import models

class file_format(models.Model):
    filename = models.CharField(max_length=255)
    nb_streams = models.IntegerField()
    nb_programs = models.IntegerField()
    format_name = models.CharField(max_length=100)
    format_long_name = models.CharField(max_length=255)
    start_time = models.CharField(max_length=32)
    duration = models.FloatField()
    size = models.BigIntegerField()
    bit_rate = models.BigIntegerField()
    probe_score = models.IntegerField()

    # Tags (many-to-one or JSONField)
    major_brand = models.CharField(max_length=50, null=True, blank=True)
    minor_version = models.CharField(max_length=50, null=True, blank=True)
    compatible_brands = models.CharField(max_length=100, null=True, blank=True)
    creation_time = models.DateTimeField(null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    location_eng = models.CharField(max_length=100, null=True, blank=True)
    android_version = models.CharField(max_length=50, null=True, blank=True)
    android_manufacturer = models.CharField(max_length=50, null=True, blank=True)
    android_model = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.filename
