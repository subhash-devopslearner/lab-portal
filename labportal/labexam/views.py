from django.shortcuts import render, redirect
from django.db.models import Count
from django.db import IntegrityError
from .models import LabExam
from .forms import LabExamForm
from django.contrib import messages

def labexam_upload(request):
    if request.method == "POST":
        form = LabExamForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "File(s) uploaded successfully!")  # success message
                return redirect('success')
            except IntegrityError:
                messages.error(request, "A record for this SAP ID already exists for the selected date.")
        else:
            # Show validation errors from the form
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field.capitalize()}: {error}")
    else:
        form = LabExamForm()
    return render(request, 'labexam/upload.html', {'form': form})



# def labexam_upload(request):
#     if request.method == "POST":
#         form = LabExamForm(request.POST, request.FILES)
#         if form.is_valid():
#             try:
#                 form.save()
#                 return redirect('success')
#             except IntegrityError:
#                 form.add_error(None, 'A record for this SAP ID already exists for the selected date.')
#     else:
#         form = LabExamForm()
#     return render(request, 'labexam/upload.html', {'form': form})

def success_view(request):
    return render(request, 'labexam/success.html')

def lab_exam_summary(request):
    # Fetch all records from the LabExam table
    lab_exams = LabExam.objects.all()

    # Group by lab_name and count the number of students in each lab    
    #lab_summary = LabExam.objects.values('lab_name').annotate(student_count=Count('sap_id', distinct=True))
    lab_summary = (
        LabExam.objects.values('lab_name', 'date')  # Group by lab_name and date
        .annotate(student_count=Count('sap_id', distinct=True))  # Count distinct sap_id
        .order_by('date', 'lab_name')  # Order by date and lab_name
    )
    
    # Calculate the total number of students
    return render(request, 'labexam/lab_exam_summary.html', {
        'lab_exams': lab_exams,
        'lab_summary': lab_summary,
    })
