from django.urls import path
from .views import labexam_upload, success_view, lab_exam_summary

urlpatterns = [
    path('upload/', labexam_upload, name='labexam_upload'),
    path('success/', success_view, name='success'),
    path('lab-exam-summary/', lab_exam_summary, name='lab_exam_summary'),    
]
