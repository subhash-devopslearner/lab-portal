from django import forms
from .models import LabExam
from django.core.exceptions import ValidationError

class LabExamForm(forms.ModelForm):
    MAX_FILE_SIZE_MB = 5  # Set the maximum file size in MB

    class Meta:
        model = LabExam
        fields = [
            'student_first_name',
            'student_last_name',
            'lab_name',
            'program',
            'branch',
            'sap_id',
            'roll_number',
            'file1_upload',
            'file2_upload',
            'file3_upload',
            'file4_upload',
            'file5_upload',
        ]
        labels = {
            'student_first_name': 'First Name',
            'student_last_name': 'Last Name',
            'lab_name': 'Lab Name',
            'program': 'Program',
            'branch': 'Branch',
            'sap_id': 'SAP ID',
            'roll_number': 'Roll Number',
            'file1_upload': 'File 1 Upload (Mandatory)',
            'file2_upload': 'File 2 Upload (Optional)',
            'file3_upload': 'File 3 Upload (Optional)',
            'file4_upload': 'File 4 Upload (Optional)',
            'file5_upload': 'File 5 Upload (Optional)',
        }
        widgets = {
            'student_first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter First Name'}),
            'student_last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Last Name'}),
            'lab_name': forms.Select(attrs={'class': 'form-select'}),
            'program': forms.Select(attrs={'class': 'form-select'}),
            'branch': forms.Select(attrs={'class': 'form-select'}),
            'sap_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter 11-digit SAP ID'}),
            'roll_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Roll Number'}),
            'file1_upload': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'file2_upload': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'file3_upload': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'file4_upload': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'file5_upload': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        sap_id = cleaned_data.get('sap_id')
        date = cleaned_data.get('date')

        if LabExam.objects.filter(sap_id=sap_id, date=date).exists():
            raise ValidationError("A record for this SAP ID already exists for the selected date.")
        return cleaned_data    

    
    def validate_file_size(self, file):
        #Helper method to validate file size.
        if file.size > self.MAX_FILE_SIZE_MB * 1024 * 1024:  # Convert MB to bytes
            raise forms.ValidationError(f"File size must not exceed {self.MAX_FILE_SIZE_MB} MB.")        
        return file
    
    def clean_file1_upload(self):
        file1 = self.cleaned_data.get('file1_upload')
        if file1:
            if not file1.name.endswith('.pdf'):
                raise forms.ValidationError("Only PDF files are allowed!")
            self.validate_file_size(file1)  # Validate file size            
        return file1
    
    def clean_file2_upload(self):
        file2 = self.cleaned_data.get('file2_upload')
        if file2:
            if not file2.name.endswith('.pdf'):
                raise forms.ValidationError("Only PDF files are allowed!")
            self.validate_file_size(file2)  # Validate file size            
        return file2
    
    def clean_file3_upload(self):
        file3 = self.cleaned_data.get('file3_upload')
        if file3:
            if not file3.name.endswith('.pdf'):
                raise forms.ValidationError("Only PDF files are allowed!")
            self.validate_file_size(file3)  # Validate file size            
        return file3
    
    def clean_file4_upload(self):
        file4 = self.cleaned_data.get('file4_upload')
        if file4:
            if not file4.name.endswith('.pdf'):
                raise forms.ValidationError("Only PDF files are allowed!")
            self.validate_file_size(file4)  # Validate file size            
        return file4
    
    def clean_file5_upload(self):
        file5 = self.cleaned_data.get('file5_upload')
        if file5:
            if not file5.name.endswith('.pdf'):
                raise forms.ValidationError("Only PDF files are allowed!")
            self.validate_file_size(file5)  # Validate file size            
        return file5