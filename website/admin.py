from django.contrib import admin
from .models import School_Information,Department, Team_Member,Event,Staff, Blog
# Register your models here.
admin.site.register(School_Information)
admin.site.register(Department)
admin.site.register(Team_Member)
admin.site.register(Event)
admin.site.register(Staff)
admin.site.register(Blog)