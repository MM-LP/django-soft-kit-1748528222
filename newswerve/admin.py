from django.contrib import admin

from .models.Activities import Activities
from .models.ASOperation import ASOperation
from .models.ArchivedContacts import ArchivedContacts
from .models.ArchivedMediaFile import ArchivedMediaFile
from .models.ArchivedMediaFolder import ArchivedMediaFolder
from .models.ArchivedMediaInFolder import ArchivedMediaInFolder
from .models.ArchivedMediaLayoutPreset import ArchivedMediaLayoutPreset
from .models.ArchivedMediaTag import ArchivedMediaTag
from .models.ArchivedPost import ArchivedPost
from .models.ArchivedPostMedia import ArchivedPostMedia
from .models.ArchivedSetDetail import ArchivedSetDetail
from .models.ArchivedSetLog import ArchivedSetLog
from .models.ArchivedTag import ArchivedTag
from .models.ArchivedTrainingDetail import ArchivedTrainingDetail
from .models.ArchivedUserPreferences import ArchivedUserPreferences
from .models.ArchivedUserProfile import ArchivedUserProfile
from .models.Autosteer import Autosteer
from .models.BoatDetail import BoatDetail
from .models.BoatDriver import BoatDriver
from .models.BoatInfo import BoatInfo 
from .models.Call import Call
from .models.Comment import Comment
from .models.ConflictLog import ConflictLog
from .models.Contacts import Contacts
from .models.CourseSet import CourseSet
from .models.CourseSurveyData import CourseSurveyData
from .models.DeviceSyncStatus import DeviceSyncStatus
from .models.DriverInfo import DriverInfo
from .models.EquipmentSetup import EquipmentSetup
from .models.FileFormat import FileFormat
from .models.Follow import Follow
from .models.GpsCourse import GpsCourse
from .models.GpsSource import GpsSource
from .models.GroupInvite import GroupInvite
from .models.Hashtag import Hashtag
from .models.Health import Health
from .models.InputValidate import InputValidate
from .models.Location import Location
from .models.Log import Log
from .models.MeasurementUnits import MeasurementUnits
from .models.MediaFile import MediaFile
from .models.MediaFolder import MediaFolder
from .models.MediaInFolder import MediaInFolder
from .models.MediaLayoutPreset import MediaLayoutPreset
from .models.MediaTag import MediaTag
from .models.Metrics import Metrics
from .models.MobileDetail import MobileDetail
from .models.MobilePermissionProfile import MobilePermissionProfile
from .models.MobileTemplate import MobileTemplate
from .models.Notification import Notification
from .models.OnboardingEvent import OnboardingEvent
from .models.Post import Post
from .models.PostHashtag import PostHashtag
from .models.PostMedia import PostMedia
from .models.ProductCat import ProductCat
from .models.ProductInfo import ProductInfo
from .models.Reaction import Reaction
from .models.SetDetail import SetDetail
from .models.SetLog import SetLog
from .models.ShareLink import ShareLink
from .models.SharedSet import SharedSet
from .models.SharedSetDetail import SharedSetDetail
from .models.SkiGroup import SkiGroup
from .models.UserPreferences import UserPreferences
from .models.Stream import Stream
from .models.SyncQueue import SyncQueue
from .models.Tag import Tag
from .models.TemplateElement import TemplateElement
from .models.TrainingDetail import TrainingDetail
from .models.UIEventLog import UIEventLog
from .models.UISettings import UISettings
from .models.UserTemplateInstance import UserTemplateInstance

@admin.register(Activities)
class ActivitiesAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Activities._meta.fields]
    search_fields = [field.name for field in Activities._meta.fields if field.name != 'id']

@admin.register(ASOperation)
class ASOperationAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ASOperation._meta.fields]
    search_fields = [field.name for field in ASOperation._meta.fields if field.name != 'id']

@admin.register(ArchivedContacts)
class ArchivedContactsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ArchivedContacts._meta.fields]
    search_fields = [field.name for field in ArchivedContacts._meta.fields if field.name != 'id']

@admin.register(ArchivedMediaFile)
class ArchivedMediaFileAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ArchivedMediaFile._meta.fields]
    search_fields = [field.name for field in ArchivedMediaFile._meta.fields if field.name != 'id']

@admin.register(ArchivedMediaFolder)
class ArchivedMediaFolderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ArchivedMediaFolder._meta.fields]
    search_fields = [field.name for field in ArchivedMediaFolder._meta.fields if field.name != 'id']

@admin.register(ArchivedMediaInFolder)
class ArchivedMediaInFolderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ArchivedMediaInFolder._meta.fields]
    search_fields = [field.name for field in ArchivedMediaInFolder._meta.fields if field.name != 'id']

@admin.register(ArchivedMediaLayoutPreset)
class ArchivedMediaLayoutPresetAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ArchivedMediaLayoutPreset._meta.fields]
    search_fields = [field.name for field in ArchivedMediaLayoutPreset._meta.fields if field.name != 'id']

@admin.register(ArchivedMediaTag)
class ArchivedMediaTagAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ArchivedMediaTag._meta.fields]
    search_fields = [field.name for field in ArchivedMediaTag._meta.fields if field.name != 'id']

@admin.register(ArchivedPost)
class ArchivedPostAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ArchivedPost._meta.fields]
    search_fields = [field.name for field in ArchivedPost._meta.fields if field.name != 'id']

@admin.register(ArchivedPostMedia)
class ArchivedPostMediaAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ArchivedPostMedia._meta.fields]
    search_fields = [field.name for field in ArchivedPostMedia._meta.fields if field.name != 'id']

@admin.register(ArchivedSetDetail)
class ArchivedSetDetailAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ArchivedSetDetail._meta.fields]
    search_fields = [field.name for field in ArchivedSetDetail._meta.fields if field.name != 'id']

@admin.register(ArchivedSetLog)
class ArchivedSetLogAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ArchivedSetLog._meta.fields]
    search_fields = [field.name for field in ArchivedSetLog._meta.fields if field.name != 'id']

@admin.register(ArchivedTag)
class ArchivedTagAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ArchivedTag._meta.fields]
    search_fields = [field.name for field in ArchivedTag._meta.fields if field.name != 'id']

@admin.register(ArchivedTrainingDetail)
class ArchivedTrainingDetailAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ArchivedTrainingDetail._meta.fields]
    search_fields = [field.name for field in ArchivedTrainingDetail._meta.fields if field.name != 'id']

@admin.register(ArchivedUserPreferences)
class ArchivedUserPreferencesAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ArchivedUserPreferences._meta.fields]
    search_fields = [field.name for field in ArchivedUserPreferences._meta.fields if field.name != 'id']

@admin.register(ArchivedUserProfile)
class ArchivedUserProfileAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ArchivedUserProfile._meta.fields]
    search_fields = [field.name for field in ArchivedUserProfile._meta.fields if field.name != 'id']

@admin.register(Autosteer)
class AutosteerAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Autosteer._meta.fields]
    search_fields = [field.name for field in Autosteer._meta.fields if field.name != 'id']

@admin.register(BoatDetail)
class BoatDetailAdmin(admin.ModelAdmin):
    list_display = [field.name for field in BoatDetail._meta.fields]
    search_fields = [field.name for field in BoatDetail._meta.fields if field.name != 'id']

@admin.register(BoatDriver)
class BoatDriverAdmin(admin.ModelAdmin):
    list_display = [field.name for field in BoatDriver._meta.fields]
    search_fields = [field.name for field in BoatDriver._meta.fields if field.name != 'id']

@admin.register(BoatInfo)
class BoatInfoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in BoatInfo._meta.fields]
    search_fields = [field.name for field in BoatInfo._meta.fields if field.name != 'id']

@admin.register(Call)
class CallAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Call._meta.fields]
    search_fields = [field.name for field in Call._meta.fields if field.name != 'id']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Comment._meta.fields]
    search_fields = [field.name for field in Comment._meta.fields if field.name != 'id']

@admin.register(ConflictLog)
class ConflictLogAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ConflictLog._meta.fields]
    search_fields = [field.name for field in ConflictLog._meta.fields if field.name != 'id']

@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Contacts._meta.fields]
    search_fields = [field.name for field in Contacts._meta.fields if field.name != 'id']

@admin.register(CourseSet)
class CourseSetAdmin(admin.ModelAdmin):
    list_display = [field.name for field in CourseSet._meta.fields]
    search_fields = [field.name for field in CourseSet._meta.fields if field.name != 'id']

@admin.register(CourseSurveyData)
class CourseSurveyDataAdmin(admin.ModelAdmin):
    list_display = [field.name for field in CourseSurveyData._meta.fields]
    search_fields = [field.name for field in CourseSurveyData._meta.fields if field.name != 'id']

@admin.register(DeviceSyncStatus)
class DeviceSyncStatusAdmin(admin.ModelAdmin):
    list_display = [field.name for field in DeviceSyncStatus._meta.fields]
    search_fields = [field.name for field in DeviceSyncStatus._meta.fields if field.name != 'id']

@admin.register(DriverInfo)
class driverAdmin(admin.ModelAdmin):
    list_display = [field.name for field in DriverInfo._meta.fields]
    search_fields = [field.name for field in DriverInfo._meta.fields if field.name != 'id']

@admin.register(EquipmentSetup)
class EquipmentSetupAdmin(admin.ModelAdmin):
    list_display = [field.name for field in EquipmentSetup._meta.fields]
    search_fields = [field.name for field in EquipmentSetup._meta.fields if field.name != 'id']

@admin.register(FileFormat)
class FileFormatAdmin(admin.ModelAdmin):
    list_display = [field.name for field in FileFormat._meta.fields]
    search_fields = [field.name for field in FileFormat._meta.fields if field.name != 'id']

@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Follow._meta.fields]
    search_fields = [field.name for field in Follow._meta.fields if field.name != 'id']

@admin.register(GpsCourse)
class GpsCourseAdmin(admin.ModelAdmin):
    list_display = [field.name for field in GpsCourse._meta.fields]
    search_fields = [field.name for field in GpsCourse._meta.fields if field.name != 'id']

@admin.register(GpsSource)
class GpsSourceAdmin(admin.ModelAdmin):
    list_display = [field.name for field in GpsSource._meta.fields]
    search_fields = [field.name for field in GpsSource._meta.fields if field.name != 'id']

@admin.register(GroupInvite)
class GroupInviteAdmin(admin.ModelAdmin):
    list_display = [field.name for field in GroupInvite._meta.fields]
    search_fields = [field.name for field in GroupInvite._meta.fields if field.name != 'id']

@admin.register(Hashtag)
class HashtagAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Hashtag._meta.fields]
    search_fields = [field.name for field in Hashtag._meta.fields if field.name != 'id']
 
@admin.register(Health)
class HealthAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Health._meta.fields]
    search_fields = [field.name for field in Health._meta.fields if field.name != 'id']
   
@admin.register(InputValidate)
class InputValidateAdmin(admin.ModelAdmin):
    list_display = [field.name for field in InputValidate._meta.fields]
    search_fields = [field.name for field in InputValidate._meta.fields if field.name != 'id']

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Location._meta.fields]
    search_fields = [field.name for field in Location._meta.fields if field.name != 'id']

@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Log._meta.fields]
    search_fields = [field.name for field in Log._meta.fields if field.name != 'id']

@admin.register(MeasurementUnits)
class MeasurementUnitsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in MeasurementUnits._meta.fields]
    search_fields = [field.name for field in MeasurementUnits._meta.fields if field.name != 'id']

@admin.register(MediaFile)
class MediaFileAdmin(admin.ModelAdmin):
    list_display = [field.name for field in MediaFile._meta.fields]
    search_fields = [field.name for field in MediaFile._meta.fields if field.name != 'id']

@admin.register(MediaFolder)
class MediaFolderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in MediaFolder._meta.fields]
    search_fields = [field.name for field in MediaFolder._meta.fields if field.name != 'id']

@admin.register(MediaInFolder)
class MediaInFolderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in MediaInFolder._meta.fields]
    search_fields = [field.name for field in MediaInFolder._meta.fields if field.name != 'id']

@admin.register(MediaLayoutPreset)
class MediaLayoutPresetAdmin(admin.ModelAdmin):
    list_display = [field.name for field in MediaLayoutPreset._meta.fields]
    search_fields = [field.name for field in MediaLayoutPreset._meta.fields if field.name != 'id']

@admin.register(MediaTag)
class MediaTagAdmin(admin.ModelAdmin):
    list_display = [field.name for field in MediaTag._meta.fields]
    search_fields = [field.name for field in MediaTag._meta.fields if field.name != 'id']

@admin.register(Metrics)
class MetricsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Metrics._meta.fields]
    search_fields = [field.name for field in Metrics._meta.fields if field.name != 'id']

@admin.register(MobileDetail)
class MobileDetailAdmin(admin.ModelAdmin):
    list_display = [field.name for field in MobileDetail._meta.fields]
    search_fields = [field.name for field in MobileDetail._meta.fields if field.name != 'id']

@admin.register(MobilePermissionProfile)
class MobilePermissionProfileAdmin(admin.ModelAdmin):
    list_display = [field.name for field in MobilePermissionProfile._meta.fields]
    search_fields = [field.name for field in MobilePermissionProfile._meta.fields if field.name != 'id']

@admin.register(MobileTemplate)
class MobileTemplateAdmin(admin.ModelAdmin):
    list_display = [field.name for field in MobileTemplate._meta.fields]
    search_fields = [field.name for field in MobileTemplate._meta.fields if field.name != 'id']

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Notification._meta.fields]
    search_fields = [field.name for field in Notification._meta.fields if field.name != 'id']

@admin.register(OnboardingEvent)
class OnboardingEventAdmin(admin.ModelAdmin):
    list_display = [field.name for field in OnboardingEvent._meta.fields]
    search_fields = [field.name for field in OnboardingEvent._meta.fields if field.name != 'id']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Post._meta.fields]
    search_fields = [field.name for field in Post._meta.fields if field.name != 'id']

@admin.register(PostHashtag)
class PostHashtagAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PostHashtag._meta.fields]
    search_fields = [field.name for field in PostHashtag._meta.fields if field.name != 'id']

@admin.register(PostMedia)
class PostMediaAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PostMedia._meta.fields]
    search_fields = [field.name for field in PostMedia._meta.fields if field.name != 'id']

@admin.register(ProductCat)
class ProductCatAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductCat._meta.fields]
    search_fields = [field.name for field in ProductCat._meta.fields if field.name != 'id']

@admin.register(ProductInfo)
class ProductInfoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductInfo._meta.fields]
    search_fields = [field.name for field in ProductInfo._meta.fields if field.name != 'id']
    
@admin.register(Reaction)
class reacionAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Reaction._meta.fields]
    search_fields = [field.name for field in Reaction._meta.fields if field.name != 'id']

@admin.register(SetDetail)
class SetDetailAdmin(admin.ModelAdmin):
    list_display = [field.name for field in SetDetail._meta.fields]
    search_fields = [field.name for field in SetDetail._meta.fields if field.name != 'id']

@admin.register(SetLog)
class SetLogAdmin(admin.ModelAdmin):
    list_display = [field.name for field in SetLog._meta.fields]
    search_fields = [field.name for field in SetLog._meta.fields if field.name != 'id']

@admin.register(ShareLink)
class ShareLinkAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ShareLink._meta.fields]
    search_fields = [field.name for field in ShareLink._meta.fields if field.name != 'id']

@admin.register(SharedSet)
class SharedSetAdmin(admin.ModelAdmin):
    list_display = [field.name for field in SharedSet._meta.fields]
    search_fields = [field.name for field in SharedSet._meta.fields if field.name != 'id']

@admin.register(SharedSetDetail)
class SharedSetDetailAdmin(admin.ModelAdmin):
    list_display = [field.name for field in SharedSetDetail._meta.fields]
    search_fields = [field.name for field in SharedSetDetail._meta.fields if field.name != 'id']

@admin.register(SkiGroup)
class SkiGroupAdmin(admin.ModelAdmin):
    list_display = [field.name for field in SkiGroup._meta.fields]
    search_fields = [field.name for field in SkiGroup._meta.fields if field.name != 'id']

@admin.register(UserPreferences)
class UserPreferencesAdmin(admin.ModelAdmin):
    list_display = [field.name for field in UserPreferences._meta.fields]
    search_fields = [field.name for field in UserPreferences._meta.fields if field.name != 'id']

@admin.register(Stream)
class StreamAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Stream._meta.fields]
    search_fields = [field.name for field in Stream._meta.fields if field.name != 'id']

@admin.register(SyncQueue)
class SyncQueueAdmin(admin.ModelAdmin):
    list_display = [field.name for field in SyncQueue._meta.fields]
    search_fields = [field.name for field in SyncQueue._meta.fields if field.name != 'id']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Tag._meta.fields]
    search_fields = [field.name for field in Tag._meta.fields if field.name != 'id']

@admin.register(TemplateElement)
class TemplateElementAdmin(admin.ModelAdmin):
    list_display = [field.name for field in TemplateElement._meta.fields]
    search_fields = [field.name for field in TemplateElement._meta.fields if field.name != 'id']

@admin.register(TrainingDetail)
class TrainingDetailAdmin(admin.ModelAdmin):
    list_display = [field.name for field in TrainingDetail._meta.fields]
    search_fields = [field.name for field in TrainingDetail._meta.fields if field.name != 'id']

@admin.register(UIEventLog)
class UIEventLogAdmin(admin.ModelAdmin):
    list_display = [field.name for field in UIEventLog._meta.fields]
    search_fields = [field.name for field in UIEventLog._meta.fields if field.name != 'id']

@admin.register(UISettings)
class UISettingsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in UISettings._meta.fields]
    search_fields = [field.name for field in UISettings._meta.fields if field.name != 'id']

@admin.register(UserTemplateInstance)
class UserTemplateInstanceAdmin(admin.ModelAdmin):
    list_display = [field.name for field in UserTemplateInstance._meta.fields]
    search_fields = [field.name for field in UserTemplateInstance._meta.fields if field.name != 'id']

