from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.template import loader
from django.template import RequestContext
from django.utils.translation import get_language_from_request

from geekjobs.stackoverflow_parser import load_json_file
from geekjobs.stackoverflow_parser import merge_json_jobs
from geekjobs.constants import bundeslander
from geekjobs.models import get_state_dict

from .forms import JobForm

default_region = 'DE'


def index(request, region=default_region):
    stackoverflow_jobs = load_json_file()
    geekjobs = get_state_dict()
    jobs = merge_json_jobs(stackoverflow_jobs, geekjobs)
    context = {'bundeslander': bundeslander, 'state': 'all states', 'jobs': jobs[region]}
    template = loader.get_template('index.html')
    return HttpResponse(template.render(context))


def new(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            context = RequestContext(request, {'form': form})
            return render(request, 'review.html', context)
    else:
        form = JobForm()
    context = RequestContext(request, {'form': form})
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
