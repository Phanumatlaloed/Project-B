# courses/forms.py
from django import forms

class SearchCourseForm(forms.Form):
    course_code = forms.CharField(label='รหัสวิชา', max_length=10)
