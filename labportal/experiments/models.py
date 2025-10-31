# experiments/models.py
from django.db import models
from datetime import datetime
from django.core.validators import RegexValidator
import re
import os

class AcademicYear(models.Model):
    year = models.CharField(max_length=7, unique=True)  # e.g., "2023-24"

    def __str__(self):
        return self.year
    
class Program(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Semester(models.Model):
    name = models.CharField(max_length=1)  # e.g., "1", "2"

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)  # e.g., "PHY101"

    def __str__(self):
        return f"{self.code} - {self.name}"
   

def slugify_name(value):
    """Convert text to lowercase, replace spaces/underscores/dashes with a single '-'."""
    value = value.lower()
    # Replace any sequence of non-alphanumeric (including spaces, underscores, dashes) with '-'
    value = re.sub(r'[^a-z0-9]+', '-', value)
    # Remove leading/trailing '-'
    return value.strip('-')

def experiment_upload_path(instance, filename):
    # Get base name and extension separately
    base, ext = os.path.splitext(filename)
    
    return (
        f"experiments/{slugify_name(instance.academic_year.year)}/"
        f"{slugify_name(instance.program.name)}/"
        f"sem-{slugify_name(instance.semester.name)}/"
        f"{slugify_name(instance.subject.code)}/"
        f"exp-{instance.experiment_number}/{slugify_name(base)}{ext.lower()}"
    )   


# def experiment_upload_path(instance, filename):        
#     # Define the storage path    
#     return f'experiments/{instance.academic_year}/{instance.program.lower()}/sem-{instance.semester}/{instance.subject}/exp-{instance.experiment_number}/{filename}'

class Experiment(models.Model):
    academic_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)    
    experiment_number = models.PositiveIntegerField()
    file1_upload = models.FileField(upload_to=experiment_upload_path, max_length=300)  # Adjust path dynamically
    file2_upload = models.FileField(upload_to=experiment_upload_path, max_length=300, blank=True, null=True)
    file3_upload = models.FileField(upload_to=experiment_upload_path, max_length=300, blank=True, null=True)
    file4_upload = models.FileField(upload_to=experiment_upload_path, max_length=300, blank=True, null=True)
    file5_upload = models.FileField(upload_to=experiment_upload_path, max_length=300, blank=True, null=True)
    file6_upload = models.FileField(upload_to=experiment_upload_path, max_length=300, blank=True, null=True)

    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:        
        ordering = ["uploaded_at"]
        constraints = [
            models.UniqueConstraint(
                fields=["academic_year", "program", "semester", "subject", "experiment_number"],
                name="unique_experiment_per_context"
            )
        ]

    def __str__(self):
        return f"{self.academic_year.year} - {self.program.name} - {self.semester.name} - {self.subject.code} - Exp - {self.experiment_number}"
