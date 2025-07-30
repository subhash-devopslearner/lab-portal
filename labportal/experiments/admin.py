from django.contrib import admin
from .models import AcademicYear, Semester, Subject, Program, Experiment

# Register your models here.
admin.site.register(AcademicYear)
admin.site.register(Semester)
admin.site.register(Subject)
admin.site.register(Program)
admin.site.register(Experiment)