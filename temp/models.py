
from django.db import models
from django.contrib.auth.models import User  # Replace with SkierInfo if needed

# -------------------- Slalom Pass Tracking --------------------

class CourseSurveyData(models.Model):
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    survey_date = models.DateField(blank=True, null=True)
    survey_tool = models.CharField(max_length=100, blank=True, null=True)
    correction_type = models.CharField(max_length=100, blank=True, null=True)
    baseline_distance = models.FloatField(blank=True, null=True)
    course_direction = models.CharField(max_length=50, blank=True, null=True)
    homologation = models.CharField(max_length=100, blank=True, null=True)
    g1_lat = models.FloatField(blank=True, null=True)
    g1_lng = models.FloatField(blank=True, null=True)
    g2_lat = models.FloatField(blank=True, null=True)
    g2_lng = models.FloatField(blank=True, null=True)
    ext_lat = models.FloatField(blank=True, null=True)
    ext_lng = models.FloatField(blank=True, null=True)
    data = models.TextField(max_length=25, blank=True, null=True)

class ASOperation(models.Model):
    ff = models.IntegerField(blank=True, null=True)
    pgain = models.IntegerField(blank=True, null=True)
    igain = models.IntegerField(blank=True, null=True)
    dgain = models.IntegerField(blank=True, null=True)
    st_target = models.IntegerField(blank=True, null=True)
    st_actual = models.IntegerField(blank=True, null=True)
    rudder_position = models.IntegerField(blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)

class Autosteer(models.Model):
    boat = models.ForeignKey('Boat', on_delete=models.SET_NULL, null=True)
    as_status = models.BooleanField(default=False)
    current_config = models.BooleanField(blank=False)
    auto_steer_system = models.CharField(max_length=255, blank=True, default='Standard')
    rudder_trim = models.FloatField(blank=True, null=True)
    imu_offset = models.FloatField(blank=True, null=True)
    gps_offset = models.FloatField(blank=True, null=True)
    update_time = models.DateTimeField(auto_now=True)

# -------------------- Media Management --------------------

class MediaFile(models.Model):
    skier = models.ForeignKey('SkierInfo', on_delete=models.CASCADE)
    filename = models.CharField(max_length=255)
    file_type = models.CharField(max_length=10, choices=[('image', 'Image'), ('video', 'Video')])
    pcloud_url = models.URLField()
    thumbnail_url = models.URLField(blank=True, null=True)
    device_model = models.CharField(max_length=100, blank=True, null=True)
    gps_lat = models.FloatField(blank=True, null=True)
    gps_lon = models.FloatField(blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

class MediaFolder(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_by = models.ForeignKey('SkierInfo', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class MediaInFolder(models.Model):
    folder = models.ForeignKey(MediaFolder, on_delete=models.CASCADE)
    media = models.ForeignKey(MediaFile, on_delete=models.CASCADE)
    position = models.IntegerField(blank=True, null=True)

# -------------------- Social Media & Interaction --------------------

class ShareLink(models.Model):
    media = models.ForeignKey(MediaFile, on_delete=models.CASCADE)
    shared_by = models.ForeignKey('SkierInfo', on_delete=models.CASCADE)
    url = models.URLField()
    access_level = models.CharField(max_length=10, choices=[('public', 'Public'), ('private', 'Private')])
    expiration = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Reaction(models.Model):
    media = models.ForeignKey(MediaFile, on_delete=models.CASCADE)
    user = models.ForeignKey('SkierInfo', on_delete=models.CASCADE)
    type = models.CharField(max_length=20)
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

class MediaTag(models.Model):
    media = models.ForeignKey(MediaFile, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

class UISettings(models.Model):
    user = models.ForeignKey('SkierInfo', on_delete=models.CASCADE)
    dark_mode = models.BooleanField(default=False)
    layout_style = models.CharField(max_length=50, choices=[('grid', 'Grid'), ('list', 'List')], default='grid')
    sidebar_collapsed = models.BooleanField(default=False)
    last_updated = models.DateTimeField(auto_now=True)

class MediaLayoutPreset(models.Model):
    user = models.ForeignKey('SkierInfo', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    json_layout = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

class UIEventLog(models.Model):
    user = models.ForeignKey('SkierInfo', on_delete=models.SET_NULL, null=True)
    event_type = models.CharField(max_length=100)
    metadata = models.JSONField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

# -------------------- Mobile UI Template System --------------------

class MobileTemplate(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    preview_image = models.ImageField(upload_to='templates/previews/', blank=True, null=True)
    base_layout = models.JSONField(help_text="JSON structure defining positioning and element layering")
    is_active = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

class TemplateElement(models.Model):
    template = models.ForeignKey(MobileTemplate, on_delete=models.CASCADE, related_name='elements')
    element_type = models.CharField(max_length=50, choices=[
        ('text', 'Text'), ('image', 'Image'), ('gif', 'GIF'), ('emoji', 'Emoji')
    ])
    content = models.TextField()
    position = models.JSONField(help_text="x, y, width, height coordinates")
    animation = models.JSONField(blank=True, null=True)
    layer = models.IntegerField(default=0)

class UserTemplateInstance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    media = models.ForeignKey('MediaFile', on_delete=models.CASCADE)
    template = models.ForeignKey(MobileTemplate, on_delete=models.SET_NULL, null=True)
    applied_elements = models.JSONField(help_text="Final user-customized layout")
    created_at = models.DateTimeField(auto_now_add=True)
