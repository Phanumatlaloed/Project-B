# courses/views.py
from django.shortcuts import render
from .forms import SearchCourseForm
from .models import Course

def search_course(request):
    courses = None
    form = SearchCourseForm(request.GET or None)
    if form.is_valid():
        course_code = form.cleaned_data['course_code']
        courses = Course.objects.filter(course_code__icontains=course_code)
    
    return render(request, 'courses/search_course.html', {'form': form, 'courses': courses})
