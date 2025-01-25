# experiments/views.py
from django.shortcuts import render, redirect
from .models import Experiment
from .forms import ExperimentUploadForm, ExperimentSearchForm

# Create your views here.
def upload_experiment(request):
    if request.method == 'POST':
        form = ExperimentUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home_experiments')
    else:
        form = ExperimentUploadForm()
    return render(request, 'experiments/upload.html', {'form': form})

def home_experiments(request):
    experiments = Experiment.objects.all()
    search_form = ExperimentSearchForm(request.GET or None)
    if search_form.is_valid():
        if search_form.cleaned_data['academic_year']:
            experiments = experiments.filter(academic_year__year=search_form.cleaned_data['academic_year'])
        if search_form.cleaned_data['semester']:
            experiments = experiments.filter(semester=search_form.cleaned_data['semester'])
        if search_form.cleaned_data['subject']:
            experiments = experiments.filter(subject=search_form.cleaned_data['subject'])
    return render(request, 'experiments/home.html', {'experiments': experiments, 'search_form': search_form})
