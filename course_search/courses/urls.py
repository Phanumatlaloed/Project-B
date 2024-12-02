# courses/urls.py
from django.urls import path
from . import views
app_name = 'courses'  # ตั้งชื่อ namespace สำหรับแอป
urlpatterns = [
    path('search/', views.search_course, name='search_course'),  # URL สำหรับค้นหารายวิชา
    path('edit/<int:id>/', views.edit_course, name='edit_course'),  # URL สำหรับแก้ไขข้อมูลรายวิชา
    path('delete/<int:id>/', views.delete_course, name='delete_course'),  # เพิ่ม URL สำหรับการลบ
]
