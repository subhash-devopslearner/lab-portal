# experiments/views.py
from django.shortcuts import render, redirect
from .models import Experiment
from .forms import ExperimentSearchForm, ExperimentUploadForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


#Create your views here.
def home_experiments(request):   
    
    experiments = Experiment.objects.all().order_by('academic_year__year','semester__name','subject__name','program__name', 'experiment_number')
    
    search_form = ExperimentSearchForm(request.GET or None)
    if search_form.is_valid():
        if search_form.cleaned_data['academic_year']:
            experiments = experiments.filter(academic_year__year=search_form.cleaned_data['academic_year'])
        if search_form.cleaned_data['semester']:
            experiments = experiments.filter(semester=search_form.cleaned_data['semester'])
        if search_form.cleaned_data['subject']:
            experiments = experiments.filter(subject=search_form.cleaned_data['subject'])
        if search_form.cleaned_data['program']:
            experiments = experiments.filter(program=search_form.cleaned_data['program'])

    return render(request, 'experiments/home.html', {'experiments': experiments, 'search_form': search_form})


@login_required
def upload_experiment(request):
    if request.user.role not in ['teacher', 'lab_assistant']:
        messages.error(request, "Access denied. You don't have permission to upload experiments.")
        return redirect('home')
    
    if request.method == 'POST':
        form = ExperimentUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home_experiments')
    else:
        form = ExperimentUploadForm()
    return render(request, 'experiments/upload.html', {'form': form})
