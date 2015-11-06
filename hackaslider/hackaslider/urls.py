"""hackaslider URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'hackaslider.views.home', name='home'),
    url(r'^configure/step-1/$', 'hackaslider.views.device_add', name='device_add'),
    url(r'^configure/step-2/$', 'hackaslider.views.network_link', name='network_link'),
    url(r'^configure/step-3/$', 'hackaslider.views.payload', name='payload'),
    url(r'^device/(?P<pk>[0-9]+)/$', 'hackaslider.views.device_config', name='device_config'),
    url(r'^admin/', include(admin.site.urls)),
]


if settings.DEBUG:
    urlpatterns += patterns('django.views.static',
                            (r'media/(?P<path>.*)', 'serve', {'document_root': settings.MEDIA_ROOT}),
    )