# courses/forms.py
from django import forms
from .models import Course  # Import โมเดล Course

class SearchCourseForm(forms.Form):
    course_code = forms.CharField(label='รหัสวิชา', max_length=10)

class CourseEditForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_code', 'course_name']
