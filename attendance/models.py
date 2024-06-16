from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Athlete(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Attendance(models.Model):
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=[('Present', 'Present'), ('Absent', 'Absent')])

    def __str__(self):
        return f"{self.athlete.name} - {self.date} - {self.status}"
