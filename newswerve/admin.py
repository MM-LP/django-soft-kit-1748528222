from django.contrib import admin

from .models.as_operation import as_operation
from .models.autosteer import autosteer
from .models.boat_detail import boat_detail
from .models.boat_info import boat_info
from .models.call import call
from .models.conflict_log import conflict_log
from .models.contacts import contacts
from .models.course import course
from .models.course_set import course_set
from .models.course_survey_data import course_survey_data
from .models.device_sync_status import device_sync_status
from .models.driver_info import driver_info
from .models.file_format import file_format
from .models.gps_course import gps_course
from .models.health import health
from .models.log import log
from .models.media_file import media_file
from .models.media_folder import media_folder
from .models.media_in_folder import media_in_folder
from .models.media_layout_preset import media_layout_preset
from .models.media_tag import media_tag
from .models.mobile_detail import mobile_detail
from .models.mobile_permission_profile import mobile_permission_profile
from .models.mobile_template import mobile_template
from .models.onboarding_event import onboarding_event
from .models.reaction import reaction
from .models.rope_detail import rope_detail
from .models.rope import rope
from .models.set_detail import set_detail
from .models.set_log import set_log
from .models.share_link import share_link
from .models.ski_detail import ski_detail
from .models.skier_info import skier_info
from .models.speed import speed
from .models.stream import stream
from .models.sync_queue import sync_queue
from .models.tag import tag
from .models.template_element import template_element
from .models.ui_event_log import ui_event_log
from .models.ui_settings import ui_settings
from .models.user_template_instance import user_template_instance
from .models.zero_off import zero_off


@admin.register(as_operation)
class as_operationAdmin(admin.ModelAdmin):
    list_display = [field.name for field in as_operation._meta.fields]
    search_fields = [field.name for field in as_operation._meta.fields if field.name != 'id']

@admin.register(autosteer)
class autosteerAdmin(admin.ModelAdmin):
    list_display = [field.name for field in autosteer._meta.fields]
    search_fields = [field.name for field in autosteer._meta.fields if field.name != 'id']

@admin.register(boat_detail)
class boat_detailAdmin(admin.ModelAdmin):
    list_display = [field.name for field in boat_detail._meta.fields]
    search_fields = [field.name for field in boat_detail._meta.fields if field.name != 'id']

@admin.register(boat_info)
class boat_infoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in boat_info._meta.fields]
    search_fields = [field.name for field in boat_info._meta.fields if field.name != 'id']

@admin.register(call)
class callAdmin(admin.ModelAdmin):
    list_display = [field.name for field in call._meta.fields]
    search_fields = [field.name for field in call._meta.fields if field.name != 'id']

@admin.register(conflict_log)
class conflict_logAdmin(admin.ModelAdmin):
    list_display = [field.name for field in conflict_log._meta.fields]
    search_fields = [field.name for field in conflict_log._meta.fields if field.name != 'id']

@admin.register(contacts)
class contactsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in contacts._meta.fields]
    search_fields = [field.name for field in contacts._meta.fields if field.name != 'id']

@admin.register(course)
class courseAdmin(admin.ModelAdmin):
    list_display = [field.name for field in course._meta.fields]
    search_fields = [field.name for field in course._meta.fields if field.name != 'id']

@admin.register(course_set)
class course_setAdmin(admin.ModelAdmin):
    list_display = [field.name for field in course_set._meta.fields]
    search_fields = [field.name for field in course_set._meta.fields if field.name != 'id']

@admin.register(course_survey_data)
class course_survey_dataAdmin(admin.ModelAdmin):
    list_display = [field.name for field in course_survey_data._meta.fields]
    search_fields = [field.name for field in course_survey_data._meta.fields if field.name != 'id']

@admin.register(device_sync_status)
class device_sync_statusAdmin(admin.ModelAdmin):
    list_display = [field.name for field in device_sync_status._meta.fields]
    search_fields = [field.name for field in device_sync_status._meta.fields if field.name != 'id']

@admin.register(driver_info)
class driverAdmin(admin.ModelAdmin):
    list_display = [field.name for field in driver_info._meta.fields]
    search_fields = [field.name for field in driver_info._meta.fields if field.name != 'id']

@admin.register(file_format)
class file_formatAdmin(admin.ModelAdmin):
    list_display = [field.name for field in file_format._meta.fields]
    search_fields = [field.name for field in file_format._meta.fields if field.name != 'id']

@admin.register(gps_course)
class gps_courseAdmin(admin.ModelAdmin):
    list_display = [field.name for field in gps_course._meta.fields]
    search_fields = [field.name for field in gps_course._meta.fields if field.name != 'id']

@admin.register(health)
class healthAdmin(admin.ModelAdmin):
    list_display = [field.name for field in health._meta.fields]
    search_fields = [field.name for field in health._meta.fields if field.name != 'id']

@admin.register(log)
class logAdmin(admin.ModelAdmin):
    list_display = [field.name for field in log._meta.fields]
    search_fields = [field.name for field in log._meta.fields if field.name != 'id']

@admin.register(media_file)
class media_fileAdmin(admin.ModelAdmin):
    list_display = [field.name for field in media_file._meta.fields]
    search_fields = [field.name for field in media_file._meta.fields if field.name != 'id']

@admin.register(media_folder)
class media_folderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in media_folder._meta.fields]
    search_fields = [field.name for field in media_folder._meta.fields if field.name != 'id']

@admin.register(media_in_folder)
class media_in_folderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in media_in_folder._meta.fields]
    search_fields = [field.name for field in media_in_folder._meta.fields if field.name != 'id']

@admin.register(media_layout_preset)
class media_layout_presetAdmin(admin.ModelAdmin):
    list_display = [field.name for field in media_layout_preset._meta.fields]
    search_fields = [field.name for field in media_layout_preset._meta.fields if field.name != 'id']

@admin.register(media_tag)
class media_tagAdmin(admin.ModelAdmin):
    list_display = [field.name for field in media_tag._meta.fields]
    search_fields = [field.name for field in media_tag._meta.fields if field.name != 'id']

@admin.register(mobile_detail)
class mobile_detailAdmin(admin.ModelAdmin):
    list_display = [field.name for field in mobile_detail._meta.fields]
    search_fields = [field.name for field in mobile_detail._meta.fields if field.name != 'id']

@admin.register(mobile_permission_profile)
class mobile_permission_profileAdmin(admin.ModelAdmin):
    list_display = [field.name for field in mobile_permission_profile._meta.fields]
    search_fields = [field.name for field in mobile_permission_profile._meta.fields if field.name != 'id']

@admin.register(mobile_template)
class mobile_templateAdmin(admin.ModelAdmin):
    list_display = [field.name for field in mobile_template._meta.fields]
    search_fields = [field.name for field in mobile_template._meta.fields if field.name != 'id']

@admin.register(onboarding_event)
class onboarding_eventAdmin(admin.ModelAdmin):
    list_display = [field.name for field in onboarding_event._meta.fields]
    search_fields = [field.name for field in onboarding_event._meta.fields if field.name != 'id']

@admin.register(reaction)
class reacionAdmin(admin.ModelAdmin):
    list_display = [field.name for field in reaction._meta.fields]
    search_fields = [field.name for field in reaction._meta.fields if field.name != 'id']

@admin.register(rope_detail)
class rope_detailAdmin(admin.ModelAdmin):
    list_display = [field.name for field in rope_detail._meta.fields]
    search_fields = [field.name for field in rope_detail._meta.fields if field.name != 'id']

@admin.register(rope)
class ropeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in rope._meta.fields]
    search_fields = [field.name for field in rope._meta.fields if field.name != 'id']

@admin.register(set_detail)
class set_detailAdmin(admin.ModelAdmin):
    list_display = [field.name for field in set_detail._meta.fields]
    search_fields = [field.name for field in set_detail._meta.fields if field.name != 'id']

@admin.register(set_log)
class set_logAdmin(admin.ModelAdmin):
    list_display = [field.name for field in set_log._meta.fields]
    search_fields = [field.name for field in set_log._meta.fields if field.name != 'id']

@admin.register(share_link)
class share_linkAdmin(admin.ModelAdmin):
    list_display = [field.name for field in share_link._meta.fields]
    search_fields = [field.name for field in share_link._meta.fields if field.name != 'id']

@admin.register(ski_detail)
class ski_detailAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ski_detail._meta.fields]
    search_fields = [field.name for field in ski_detail._meta.fields if field.name != 'id']

@admin.register(skier_info)
class skier_infoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in skier_info._meta.fields]
    search_fields = [field.name for field in skier_info._meta.fields if field.name != 'id']

@admin.register(speed)
class speedAdmin(admin.ModelAdmin):
    list_display = [field.name for field in speed._meta.fields]
    search_fields = [field.name for field in speed._meta.fields if field.name != 'id']

@admin.register(stream)
class streamAdmin(admin.ModelAdmin):
    list_display = [field.name for field in stream._meta.fields]
    search_fields = [field.name for field in stream._meta.fields if field.name != 'id']

@admin.register(sync_queue)
class sync_queueAdmin(admin.ModelAdmin):
    list_display = [field.name for field in sync_queue._meta.fields]
    search_fields = [field.name for field in sync_queue._meta.fields if field.name != 'id']

@admin.register(tag)
class tagAdmin(admin.ModelAdmin):
    list_display = [field.name for field in tag._meta.fields]
    search_fields = [field.name for field in tag._meta.fields if field.name != 'id']

@admin.register(template_element)
class template_elementAdmin(admin.ModelAdmin):
    list_display = [field.name for field in template_element._meta.fields]
    search_fields = [field.name for field in template_element._meta.fields if field.name != 'id']

@admin.register(ui_event_log)
class ui_event_logAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ui_event_log._meta.fields]
    search_fields = [field.name for field in ui_event_log._meta.fields if field.name != 'id']

@admin.register(ui_settings)
class ui_settingsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ui_settings._meta.fields]
    search_fields = [field.name for field in ui_settings._meta.fields if field.name != 'id']

@admin.register(user_template_instance)
class user_template_instanceAdmin(admin.ModelAdmin):
    list_display = [field.name for field in user_template_instance._meta.fields]
    search_fields = [field.name for field in user_template_instance._meta.fields if field.name != 'id']

@admin.register(zero_off)
class zero_offAdmin(admin.ModelAdmin):
    list_display = [field.name for field in zero_off._meta.fields]
    search_fields = [field.name for field in zero_off._meta.fields if field.name != 'id']
