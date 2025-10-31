# Create your models here.
import os
from django.db import models
from datetime import datetime
from django.core.validators import RegexValidator

def labexam_upload_path(instance, filename):
    # Get current date in YYYY-MM-DD format
    current_date = datetime.now().strftime("%Y-%m-%d")
    # Define the storage path
    return f'labexam/{current_date}/{instance.lab_name}/{instance.program}/{instance.branch}/{instance.student_first_name}-{instance.student_last_name}-{instance.sap_id}-{filename}'

class LabExam(models.Model):
    PROGRAM_CHOICES = [
        ('BTech', 'BTech'),
        ('MBATech', 'MBATech'),
    ]
    BRANCH_CHOICES = [
        ('CS', 'CS'),
        ('CE', 'CE'),
        ('IT', 'IT'),
        ('AIML', 'AIML'),
        ('CS-DS', 'CS-DS'),
    ]
    LAB_CHOICES = [
        ('CC-I', 'CC-I'),
        ('CC-II', 'CC-II'),
        ('PL-I', 'PL-I'),
        ('DATABASE', 'DATABASE'),
        ('PL-II', 'PL-II'),
        ('PROJECT-I ', 'PROJECT-I'),
        ('DSP', 'DSP'),
        ('CN', 'CN'),
        ('SE', 'SE'),
        ('APL', 'APL'),
        ('LANGUAGE', 'LANGUAGE'),
        ('SP', 'SP'),
        ('ACN', 'ACN'),
        ('PROJECT-II', 'PROJECT-II'),
        ('SS', 'SS'),
        ('CAD', 'CAD'),
        ('AIML-Lab', 'AIML-Lab'),
    ]

    student_first_name = models.CharField(max_length=50)
    student_last_name = models.CharField(max_length=50)    
    lab_name = models.CharField(max_length=50, choices=LAB_CHOICES)
    program = models.CharField(max_length=50, choices=PROGRAM_CHOICES)
    branch = models.CharField(max_length=50, choices=BRANCH_CHOICES)

    sap_id = models.CharField(
        max_length=11,
        #unique=True,  # Enforce uniqueness for sap_id
        validators=[RegexValidator(regex=r'^\d{11}$', message='SAP ID must be an 11-digit number.')]
    )
    
    roll_number = models.CharField(
        max_length=4,
        validators=[RegexValidator(
            regex=r'^[A-Za-z]\d{3}$', message='Roll number must be like A123')]
    )
    
    #date_time = models.DateTimeField(auto_now_add=True)  
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
        
    file1_upload = models.FileField(upload_to=labexam_upload_path)

    file2_upload = models.FileField(upload_to=labexam_upload_path, blank=True, null=True)
    file3_upload = models.FileField(upload_to=labexam_upload_path, blank=True, null=True)
    file4_upload = models.FileField(upload_to=labexam_upload_path, blank=True, null=True)
    file5_upload = models.FileField(upload_to=labexam_upload_path, blank=True, null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['sap_id', 'date'], name='unique_sap_id_date')
        ]

    def __str__(self):
        return f"{self.student_first_name} {self.student_last_name} - {self.sap_id}"
