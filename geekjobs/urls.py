"""geekjobs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns

from geekjobs import views

urlpatterns = []

urlpatterns += i18n_patterns(
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='home'),
    url(r'^(?P<region>[A-Z]+$)', views.index),
    url(r'^new/$', views.new, name='new'),
    url(r'^add_job/$', views.add_job, name='add_job'),
)