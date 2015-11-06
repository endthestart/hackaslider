from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from .forms import DeviceForm
from .models import Device


import logging
logger = logging.getLogger("default")


def home(request, template_name='home.html'):
    context = {}
    return render_to_response(template_name, context, RequestContext(request))


def device_add(request, template_name='device_add.html'):
    device_form = DeviceForm()
    if request.method == 'POST':
        device_form = DeviceForm(request.POST)
        if device_form.is_valid():
            device_instance = device_form.save()
            return HttpResponseRedirect(reverse('device_config', args=(device_instance.id,)))

    context = {
        'device_form': device_form,
    }
    return render_to_response(template_name, context, RequestContext(request))

def device_config(request, pk=None, template_name='device_config.html'):
    device_instance = get_object_or_404(Device, pk=pk)
    device_form = DeviceForm(instance=device_instance)
    if request.method == 'POST':
        device_form = DeviceForm(request.POST, instance=device_instance)
        if device_form.is_valid():
            device_instance = device_form.save()

    context = {
        'device_form': device_form,
        'device_instance': device_instance,
    }
    return render_to_response(template_name, context, RequestContext(request))