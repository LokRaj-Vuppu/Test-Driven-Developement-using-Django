from django.contrib import admin
from accounts.models import Profile, PlatformStatistics

# Register your models here.

admin.site.register(Profile)
admin.site.register(PlatformStatistics)
