# experiments/models.py
from django.db import models
from datetime import datetime
from django.core.validators import RegexValidator

class AcademicYear(models.Model):
    year = models.CharField(max_length=9, unique=True)  # e.g., "2023-2024"

    def __str__(self):
        return self.year

class Semester(models.Model):
    name = models.CharField(max_length=50)  # e.g., "Semester 1", "Semester 2"

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)  # e.g., "PHY101"

    def __str__(self):
        return f"{self.code} - {self.name}"

class Programme(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
def experiment_upload_path(instance, filename):        
    # Define the storage path    
    return f'experiments/{instance.academic_year}/{instance.programme}/{instance.semester}/{instance.subject}/{instance.experiment_number}-{filename}'

class Experiment(models.Model):
    academic_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    programme = models.ForeignKey(Programme, on_delete=models.CASCADE)
    experiment_number = models.PositiveIntegerField()
    file1_upload = models.FileField(upload_to=experiment_upload_path, max_length=300)  # Adjust path dynamically
    file2_upload = models.FileField(upload_to=experiment_upload_path, max_length=300, blank=True, null=True)
    file3_upload = models.FileField(upload_to=experiment_upload_path, max_length=300, blank=True, null=True)
    file4_upload = models.FileField(upload_to=experiment_upload_path, max_length=300, blank=True, null=True)

    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["uploaded_at"]

    def __str__(self):
        return f"Exp {self.experiment_number} - {self.subject.name} ({self.academic_year.year})"
