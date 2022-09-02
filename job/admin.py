from django.contrib import admin
from .models import Job,Apply,Jobcategory
from import_export.admin import ImportExportModelAdmin
admin.site.register(Jobcategory)
admin.site.register(Apply)
@admin.register(Job)
class JobAdmin(ImportExportModelAdmin):
    pass


