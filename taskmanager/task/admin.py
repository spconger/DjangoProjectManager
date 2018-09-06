from django.contrib import admin
from .models import ProjectType, ProjectDef, WorkLog

# Register your models here.
admin.site.register(ProjectType)
admin.site.register(ProjectDef)
admin.site.register(WorkLog)