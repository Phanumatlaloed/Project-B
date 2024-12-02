# courses/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.search_course, name='home'),  # หน้าแรกที่แสดงหน้าค้นหารายวิชา
    path('search/', views.search_course, name='search_course'),  # เส้นทางสำหรับการค้นหาวิชา
]
