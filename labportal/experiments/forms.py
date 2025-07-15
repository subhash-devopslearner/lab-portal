# experiments/forms.py
from django import forms
from .models import Experiment, AcademicYear, Semester, Subject

class ExperimentSearchForm(forms.Form):
    academic_year = forms.ModelChoiceField(
        queryset=AcademicYear.objects.all(),
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Academic Year",
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
            'semester',
            'subject',
            'programme',
            'experiment_number',
            'file',
        ]
        widgets = {
            'academic_year': forms.Select(attrs={'class': 'form-control'}),
            'semester': forms.Select(attrs={'class': 'form-control'}),
            'subject': forms.Select(attrs={'class': 'form-control'}),
            'programme': forms.Select(attrs={'class': 'form-control'}),
            'experiment_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'file': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }