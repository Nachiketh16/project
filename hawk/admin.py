from django.contrib import admin
from .models import heroImage, Updates, Athlete

# Register your models here.
admin.site.register(heroImage)
admin.site.register(Updates)
admin.site.register(Athlete)