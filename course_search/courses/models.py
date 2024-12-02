# courses/models.py
from django.db import models

class Course(models.Model):
    course_code = models.CharField(max_length=10)
    course_name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.course_code}: {self.course_name}'
