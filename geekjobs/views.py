import stripe
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.template import loader
from django.utils.translation import get_language_from_request
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from geekjobs.stackoverflow_parser import load_stackoverflow_jobs
from geekjobs.stackoverflow_parser import merge_dict_jobs
from geekjobs.stackoverflow_parser import eu_countries_sorted
from geekjobs.stackoverflow_parser import eu_countries

from geekjobs.models import load_model_jobs
from geekjobs.forms import JobForm

default_region = 'EU'


def index(request, region=default_region):
    stackoverflow_jobs = load_stackoverflow_jobs()
    geekjobs = load_model_jobs()
    jobs = merge_dict_jobs(stackoverflow_jobs, geekjobs)
    context = {'countries': eu_countries_sorted, 'jobs': jobs[region],
               'country': eu_countries[region], 'region': region}
    template = loader.get_template('index.html')
    return HttpResponse(template.render(context))


def new(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            context = {'form': form,
                       'country': eu_countries_sorted[form['state'].data],
                       'stripe_data_label': _('Pay for your Ad'),
                       'stripe_data_image': static('geekjobs.png'),
                       'stripe_data_key': settings.STRIPE_DATA_KEY,
                       'stripe_data_description': _('Pay for your advertisement.')}
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
            stripe.api_key = settings.STRIPE_TEST_API_KEY
            token = request.POST['stripeToken']
            # Charge the user's card:
            charge = stripe.Charge.create(
                amount=5000,
                currency="eur",
                description="Pay for your advertisement at geekjobs",
                source=token,
            )
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
