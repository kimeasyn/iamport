from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import login
from .views import profile

urlpatterns = [
    url(r'^login/$', login, name='login', kwargs={
        'template_name': 'accounts/login.html',
    }),
    url(r'^profile/$', profile, name='profile'),
]
