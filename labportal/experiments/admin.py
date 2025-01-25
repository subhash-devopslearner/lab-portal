from django.contrib import admin
from .models import AcademicYear, Semester, Subject, Programme, Experiment

# Register your models here.
admin.site.register(AcademicYear)
admin.site.register(Semester)
admin.site.register(Subject)
admin.site.register(Programme)
admin.site.register(Experiment)