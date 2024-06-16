from django.urls import path
from . import views

urlpatterns = [
    path('mark/', views.mark_attendance, name='mark'),
    path('list/', views.attendance_list, name='attendance_list'),
]
