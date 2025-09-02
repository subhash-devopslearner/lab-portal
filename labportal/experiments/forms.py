# experiments/forms.py
from django import forms
from .models import Experiment, AcademicYear, Program, Semester, Subject
import os
from django.core.exceptions import ValidationError

class ExperimentSearchForm(forms.Form):
    academic_year = forms.ModelChoiceField(
        queryset=AcademicYear.objects.all(),
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Academic Year",
    )
    program = forms.ModelChoiceField(
        queryset=Program.objects.all(),
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Program",
    )
    semester = forms.ModelChoiceField(
        queryset=Semester.objects.all(),
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Semester",
    )
    subject = forms.ModelChoiceField(
        queryset=Subject.objects.all(),
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Subject",
    )
    



class ExperimentUploadForm(forms.ModelForm):
    class Meta:
        model = Experiment
        fields = [
            'academic_year',
            'program',
            'semester',
            'subject',            
            'experiment_number',
            'file1_upload',
            'file2_upload',
            'file3_upload',
            'file4_upload',
            'file5_upload',
            'file6_upload',            
        ]
        widgets = {
            'academic_year': forms.Select(attrs={'class': 'form-control'}),
            'program': forms.Select(attrs={'class': 'form-control'}),
            'semester': forms.Select(attrs={'class': 'form-control'}),
            'subject': forms.Select(attrs={'class': 'form-control'}),            
            'experiment_number': forms.NumberInput(attrs={'class': 'form-control'}),            
            'file1_upload': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'file2_upload': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'file3_upload': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'file4_upload': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'file5_upload': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'file6_upload': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

        labels = {
            'file1_upload': 'Part A (Mandatory)',
            'file2_upload': 'Part B (Optional)',
            'file3_upload': 'Experiment List (Optional)',
            'file4_upload': 'Course Policy (Optional)',
            'file5_upload': 'Extra File (Optional)',
            'file6_upload': 'Solution File (Optional)',            
        }

def clean(self):
    cleaned_data = super().clean()

    # Define allowed extensions per field
    allowed_extensions_map = {
        'file1_upload': ['.pdf', '.doc', '.docx'],
        'file2_upload': ['.pdf', '.doc', '.docx'],
        'file3_upload': ['.pdf', '.doc', '.docx'],
        'file4_upload': ['.pdf', '.doc', '.docx'],
        'file5_upload': ['.pdf', '.doc', '.docx', '.ppt', '.pptx', '.xls', '.xlsx', '.zip', '.rar'],
        'file6_upload': ['.pdf', '.doc', '.docx', '.ppt', '.pptx', '.xls', '.xlsx', '.zip', '.rar'],
    }

    # Define max size per field (in bytes)
    max_size_map = {
        'file1_upload': 5 * 1024 * 1024,   # 5 MB
        'file2_upload': 5 * 1024 * 1024,
        'file3_upload': 5 * 1024 * 1024,
        'file4_upload': 5 * 1024 * 1024,
        'file5_upload': 25 * 1024 * 1024,  # 25 MB
        'file6_upload': 25 * 1024 * 1024        
    }

    for field_name, allowed_extensions in allowed_extensions_map.items():
        file = cleaned_data.get(field_name)
        if file:
            ext = os.path.splitext(file.name)[1].lower()
            if ext not in allowed_extensions:
                self.add_error(
                    field_name,
                    f"Invalid file type. Allowed types: {', '.join(allowed_extensions)}"
                )
            if file.size > max_size_map[field_name]:
                self.add_error(
                    field_name,
                    f"File size must be under {max_size_map[field_name] // (1024 * 1024)} MB."
                )
                
