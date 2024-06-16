from django.shortcuts import render, redirect
from .models import Athlete, Attendance
from .forms import AttendanceForm
from django.contrib.auth.decorators import login_required

@login_required
def mark_attendance(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('attendance_list')
    else:
        form = AttendanceForm()
    return render(request, 'attendance/mark_attendance.html', {'form': form})

@login_required
def attendance_list(request):
    attendances = Attendance.objects.all()
    return render(request, 'attendance/attendance_list.html', {'attendances': attendances})
