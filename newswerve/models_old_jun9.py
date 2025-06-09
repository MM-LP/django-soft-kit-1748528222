"""
Auto-generated Django models based on the comparison between models.py and doc_rptObjects.pdf
All missing fields and relationships have been added.
"""

from django.db import models

class ASOperation(models.Model):
    ff = models.IntegerField(blank=True, null=True)
    pgain = models.IntegerField(blank=True, null=True)
    igain = models.IntegerField(blank=True, null=True)
    period = models.IntegerField(blank=True, null=True)
    damping = models.IntegerField(blank=True, null=True)
    xte_i = models.IntegerField(blank=True, null=True)
    max_g = models.IntegerField(blank=True, null=True)
    wp_radius = models.IntegerField(blank=True, null=True)
    sam = models.IntegerField(blank=True, null=True)
    srm = models.IntegerField(blank=True, null=True)
    srsm = models.IntegerField(blank=True, null=True)
    min_wp_dist = models.IntegerField(blank=True, null=True)
    min_speed = models.IntegerField(blank=True, null=True)
    override = models.IntegerField(blank=True, null=True)
    shift_amt = models.IntegerField(blank=True, null=True)
    gps_offset_y = models.IntegerField(blank=True, null=True)
    spd_scale = models.IntegerField(blank=True, null=True)
    servo1_trim = models.IntegerField(blank=True, null=True)
    servo2_trim = models.IntegerField(blank=True, null=True)
    ie_wp_radius = models.IntegerField(blank=True, null=True)
    ie_scale_dist = models.IntegerField(blank=True, null=True)
    ie_engage_scale = models.CharField(max_length=255, blank=True, null=True)

class Autosteer(models.Model):
    boat = models.ForeignKey('Boat', on_delete=models.SET_NULL, null=True)
    as_status = models.BooleanField(default=False)
    current_config = models.BooleanField(blank=False)
    auto_steer_system = models.CharField(max_length=255, blank=True, default='Standard')
    vehicle_profile = models.IntegerField(blank=True, null=True)
    roll = models.IntegerField(blank=True, null=True)
    pitch = models.IntegerField(blank=True, null=True)
    yaw = models.IntegerField(blank=True, null=True)
    imu_x_offset = models.IntegerField(blank=True, null=True)
    imu_y_offset = models.IntegerField(blank=True, null=True)
    imu_z_offset = models.IntegerField(blank=True, null=True)
    gps1_x_offset = models.IntegerField(blank=True, null=True)
    gps1_y_offset = models.IntegerField(blank=True, null=True)
    gps1_z_offset = models.IntegerField(blank=True, null=True)
    gps2_x_offset = models.IntegerField(blank=True, null=True)
    gps2_y_offset = models.IntegerField(blank=True, null=True)
    gps2_z_offset = models.IntegerField(blank=True, null=True)
    trim_pitch = models.IntegerField(blank=True, null=True)
    trim_roll = models.IntegerField(blank=True, null=True)
    gyros_x = models.IntegerField(blank=True, null=True)
    gyros_y = models.IntegerField(blank=True, null=True)
    gyros_z = models.IntegerField(blank=True, null=True)
    compass_cal = models.BooleanField(default=False)
    imu_cal = models.BooleanField(default=False)
    period = models.IntegerField(blank=True, null=True)
    damping = models.IntegerField(blank=True, null=True)
    xtrack_i = models.IntegerField(blank=True, null=True)
    last_update = models.DateTimeField(blank=True, null=True)

# Remaining models would be defined here similarly...

class BoatDetail(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True)
    length = models.FloatField(null=True)
    width = models.FloatField(null=True)
    brand = models.CharField(max_length=255, blank=True, null=True)
    model = models.CharField(max_length=255, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=255, blank=True, null=True)

class Contact(models.Model):
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    zip_code = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    company = models.CharField(max_length=100, blank=True, null=True)
    notes = models.TextField(blank=True)

class Boat(models.Model):
    detail = models.ForeignKey(BoatDetail, on_delete=models.CASCADE)
    registration_number = models.CharField(max_length=100, blank=True, null=True)
    owner = models.ForeignKey(Contact, on_delete=models.SET_NULL, null=True)

class Call(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    call_time = models.DateTimeField(blank=True, null=True)
    subject = models.CharField(max_length=255, blank=True, null=True)
    notes = models.TextField(blank=True)

class Course(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    contact_1 = models.CharField(max_length=100, blank=True, null=True)
    contact_2 = models.CharField(max_length=100, blank=True, null=True)
    course_type = models.CharField(max_length=100, blank=True, null=True)
    coordinate_source = models.CharField(max_length=255, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

class CourseSurveyData(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    survey_date = models.DateField(blank=True, null=True)
    survey_tool = models.CharField(max_length=100,  blank=True, null=True)
    correction_type = models.CharField(max_length=100,  blank=True, null=True)
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

class Driver(models.Model):
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    license_number = models.CharField(max_length=50, blank=True, null=True)
    contact = models.ForeignKey(Contact, on_delete=models.SET_NULL, null=True)

class GPS(models.Model):
    timestamp = models.DateTimeField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    speed = models.FloatField(null=True, blank=True)
    heading = models.FloatField(null=True, blank=True)
    correction_source = models.CharField(max_length=100, null=True, blank=True)
    rtk_receiver_provider = models.CharField(max_length=100, null=True, blank=True)
    base_station_lat = models.FloatField(null=True, blank=True)
    base_station_lng = models.FloatField(null=True, blank=True)
    base_station_height = models.FloatField(null=True, blank=True)
    surveyed_in = models.BooleanField(default=False)
    ntrip_username = models.CharField(max_length=100, blank=True, null=True)

class GPSCourse(models.Model):
    coordinate_source = models.CharField(max_length=255, blank=True, null=True)

class Health(models.Model):
    fatigue_level = models.IntegerField(blank=True, null=True)
    sleep_hours = models.FloatField(null=True, blank=True)
    hydration = models.IntegerField(null=True, blank=True)
    mood = models.CharField(max_length=100, blank=True, null=True)

class Log(models.Model):
    file = models.TextField(max_length=100, blank=True, null=True)
    log_level = models.IntegerField(null=True, blank=True)

class Rope(models.Model):
    brand = models.CharField(max_length=100, blank=True, null=True)
    color = models.CharField(max_length=50, blank=True, null=True)

class RopeDetail(models.Model):
    rope = models.ForeignKey(Rope, on_delete=models.CASCADE)
    section_length = models.FloatField(blank=True, null=True)
    section_color = models.CharField(max_length=50, blank=True, null=True)

class SkiDetail(models.Model):
    brand = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)
    length_cm = models.IntegerField(blank=True, null=True)

class Speed(models.Model):
    kmph = models.FloatField(blank=True, null=True)

class ZeroOff(models.Model):
    setting = models.CharField(max_length=100, blank=True, null=True)

class SkierInfo(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    age = models.IntegerField(null=True, blank=True)
    rope = models.ForeignKey(Rope, on_delete=models.SET_NULL, null=True)
    ski = models.ForeignKey(SkiDetail, on_delete=models.SET_NULL, null=True)
    speed = models.ForeignKey(Speed, on_delete=models.SET_NULL, null=True)
    zerooff = models.ForeignKey(ZeroOff, on_delete=models.SET_NULL, null=True)
    partner_id = models.IntegerField(null=True, blank=True)
    children_id = models.IntegerField(null=True, blank=True)

class Set(models.Model):
    skier = models.ForeignKey(SkierInfo, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    boat = models.ForeignKey(Boat, on_delete=models.SET_NULL, null=True)
    driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True)
    coach = models.CharField(max_length=255, null=True, blank=True)
    log = models.ForeignKey(Log, on_delete=models.SET_NULL, null=True)
    session_number = models.IntegerField(blank=True, null=True)
    event = models.CharField(max_length=255, blank=True, null=True)
    datetime = models.DateTimeField(blank=True, null=True)

class SetDetail(models.Model):
    session_number = models.IntegerField(blank=True, null=True)
    pass_number = models.IntegerField(blank=True, null=True)
    pass_time = models.DateTimeField(blank=True, null=True)
    rope_length = models.IntegerField(blank=True, null=True)
    pass_speed = models.IntegerField(blank=True, null=True)
    zero_off = models.IntegerField(blank=True, null=True)
    balls = models.IntegerField(blank=True, null=True)
    personal_best = models.BooleanField(default=False)
    pb_term = models.CharField(max_length=255, blank=True, null=True)
    event = models.CharField(max_length=255, blank=True, null=True)
    as_mode = models.BooleanField(blank=False)
    competition = models.IntegerField(null=True, blank=True)

class CourseSet(models.Model):
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    session_date = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"Session for {self.course} on {self.session_date}"

class Format(models.Model):
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


class Stream(models.Model):
    format = models.ForeignKey(Format, related_name='streams', on_delete=models.CASCADE)
    index = models.IntegerField()
    codec_name = models.CharField(max_length=50)
    codec_long_name = models.CharField(max_length=255)
    profile = models.CharField(max_length=50, null=True, blank=True)
    codec_type = models.CharField(max_length=20)
    codec_tag_string = models.CharField(max_length=10)
    codec_tag = models.CharField(max_length=20)
    width = models.IntegerField(null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)
    coded_width = models.IntegerField(null=True, blank=True)
    coded_height = models.IntegerField(null=True, blank=True)
    pix_fmt = models.CharField(max_length=50, null=True, blank=True)
    level = models.IntegerField(null=True, blank=True)
    color_range = models.CharField(max_length=50, null=True, blank=True)
    color_space = models.CharField(max_length=50, null=True, blank=True)
    color_transfer = models.CharField(max_length=50, null=True, blank=True)
    color_primaries = models.CharField(max_length=50, null=True, blank=True)
    field_order = models.CharField(max_length=20, null=True, blank=True)
    refs = models.IntegerField(null=True, blank=True)
    r_frame_rate = models.CharField(max_length=20)
    avg_frame_rate = models.CharField(max_length=20)
    time_base = models.CharField(max_length=20)
    start_pts = models.BigIntegerField(null=True, blank=True)
    start_time = models.FloatField()
    duration_ts = models.BigIntegerField(null=True, blank=True)
    duration = models.FloatField()
    bit_rate = models.BigIntegerField(null=True, blank=True)
    nb_frames = models.IntegerField(null=True, blank=True)
    extradata_size = models.IntegerField(null=True, blank=True)

    # Stream Tags
    creation_time = models.DateTimeField(null=True, blank=True)
    language = models.CharField(max_length=10, null=True, blank=True)
    handler_name = models.CharField(max_length=100, null=True, blank=True)
    vendor_id = models.CharField(max_length=20, null=True, blank=True)

    # Dispositions
    disposition_default = models.BooleanField(default=False)
    disposition_dub = models.BooleanField(default=False)
    disposition_original = models.BooleanField(default=False)
    disposition_comment = models.BooleanField(default=False)
    disposition_lyrics = models.BooleanField(default=False)
    disposition_karaoke = models.BooleanField(default=False)
    disposition_forced = models.BooleanField(default=False)
    disposition_hearing_impaired = models.BooleanField(default=False)
    disposition_visual_impaired = models.BooleanField(default=False)
    disposition_clean_effects = models.BooleanField(default=False)
    disposition_attached_pic = models.BooleanField(default=False)
    disposition_timed_thumbnails = models.BooleanField(default=False)
    disposition_captions = models.BooleanField(default=False)
    disposition_descriptions = models.BooleanField(default=False)
    disposition_metadata = models.BooleanField(default=False)
    disposition_dependent = models.BooleanField(default=False)
    disposition_still_image = models.BooleanField(default=False)

    def __str__(self):
        return f"Stream {self.index} - {self.codec_type} ({self.codec_name})"
