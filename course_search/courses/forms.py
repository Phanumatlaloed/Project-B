# courses/forms.py
# courses/forms.py
from django import forms

class SearchCourseForm(forms.Form):
    course_name = forms.CharField(max_length=200, required=False, label='ชื่อวิชา')
