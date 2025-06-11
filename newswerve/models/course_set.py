from django.db import models
from .course import course 

class course_set(models.Model):
    course = models.ForeignKey(course, on_delete=models.CASCADE)
    session_date = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"Session for {self.course} on {self.session_date}"
