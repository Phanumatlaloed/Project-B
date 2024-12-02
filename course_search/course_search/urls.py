"""
URL configuration for course_search project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# course_search/urls.py
from django.contrib import admin
from django.urls import path, include
from courses import views  # เพิ่มการ import views จากแอป courses

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.search_course, name='home'),  # ทำให้ URL '/' เชื่อมโยงไปที่ search_course
    path('courses/', include('courses.urls')),  # เชื่อมโยง URL ของแอป courses
]


