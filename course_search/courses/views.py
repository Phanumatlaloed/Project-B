# courses/views.py
# courses/views.py
from django.shortcuts import render
from .forms import SearchCourseForm
from .models import Course

def search_course(request):
    courses = None
    form = SearchCourseForm(request.GET or None)
    if form.is_valid():
        course_name = form.cleaned_data['course_name']  # ค้นหาจากชื่อวิชา
        courses = Course.objects.filter(course_name__icontains=course_name)  # ใช้การค้นหาจากชื่อวิชา
    
    return render(request, 'courses/search_course.html', {'form': form, 'courses': courses})
