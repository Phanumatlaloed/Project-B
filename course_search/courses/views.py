# courses/views.py
# courses/views.py
from django.shortcuts import render, get_object_or_404, redirect 
from .models import Course
from .forms import SearchCourseForm, CourseEditForm

def search_course(request):
    courses = None
    form = SearchCourseForm(request.GET or None)
    if form.is_valid():
        course_code = form.cleaned_data['course_code']
        courses = Course.objects.filter(course_code__icontains=course_code)
    
    return render(request, 'courses/course_search.html', {'form': form, 'courses': courses})

def edit_course(request, id):
    course = Course.objects.get(id=id)
    if request.method == 'POST':
        form = CourseEditForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('courses:search_course')  # เปลี่ยนเส้นทางไปหน้าค้นหารายวิชา
    else:
        form = CourseEditForm(instance=course)

    return render(request, 'courses/edit_course.html', {'form': form})

def delete_course(request, id):
    # ดึงข้อมูลรายวิชาที่ต้องการลบ
    course = get_object_or_404(Course, id=id)

    if request.method == 'POST':
        course.delete()  # ลบรายวิชาจากฐานข้อมูล
        return redirect('courses:search_course')  # เปลี่ยนเส้นทางไปหน้าค้นหารายวิชา

    return render(request, 'courses/confirm_delete.html', {'course': course})