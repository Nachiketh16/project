from django.contrib import admin
from .models import heroImage, Athlete, News, training

# Register your models here.
admin.site.register(heroImage)
admin.site.register(News)
admin.site.register(Athlete)
admin.site.register(training)