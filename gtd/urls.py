"""superlists URL Configuration

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
from django.conf.urls import patterns, url
from gtd.views import *

urlpatterns = [
    url(r'^overview/$', view_all),
    url(r'^login/$', login),
    url(r'^pomodoro/(\d+)/$', view_pomodoro),
    # url(r'^pomodoro/new$', new_pomodoro),
    url(r'^schedule/$', view_schedule),
    url(r'^schedule/new$', new_schedule),
    url(r'^health/$', view_health),
    url(r'^health/import/$', import_health),
    url(r'^health/export/$', export_health),
]
