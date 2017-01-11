from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.template import loader
from django.utils.translation import get_language_from_request

from geekjobs.stackoverflow_parser import load_stackoverflow_jobs
from geekjobs.stackoverflow_parser import merge_dict_jobs
from geekjobs.stackoverflow_parser import eu_countries_sorted
from geekjobs.models import load_model_jobs
from geekjobs.forms import JobForm

default_region = 'EU'


def index(request, region=default_region):
    stackoverflow_jobs = load_stackoverflow_jobs()
    geekjobs = load_model_jobs()
    jobs = merge_dict_jobs(stackoverflow_jobs, geekjobs)
    context = {'bundeslander': eu_countries_sorted, 'state': 'all states', 'jobs': jobs[region], 'country': region}
    template = loader.get_template('index.html')
    return HttpResponse(template.render(context))


def new(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            context = {'form': form}
            return render(request, 'review.html', context)
    else:
        form = JobForm()
    context = {'form': form}
    return render(request, 'new.html', context)


def add_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return new(request)


def terms(request):
    lang = get_language_from_request(request, check_path=True)
    html = 'terms.html'
    if lang == 'es':
        html = 'es_terms.html'
    elif lang == 'de':
        html = 'de_terms.html'
    return render(request, html)


def privacy(request):
    lang = get_language_from_request(request, check_path=True)
    html = 'privacy.html'
    if lang == 'es':
        html = 'es_privacy.html'
    elif lang == 'de':
        html = 'de_privacy.html'
    return render(request, html)
