from django.db import models
from .Location import Location 
from .SetLog import SetLog
from django.utils import timezone

class CourseSet(models.Model):
    set_id = models.ForeignKey(SetLog, on_delete=models.SET_NULL, null=True)
    course_id = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    session_date = models.DateTimeField(auto_now=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Session for {self.course} on {self.session_date}"
