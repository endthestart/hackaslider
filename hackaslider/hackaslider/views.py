from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from .forms import ShortDeviceForm, DeviceForm, NetworkStructureForm, NetworkLinkForm, ProtocolForm
from .models import Device, NetworkStructure, NetworkLink, Protocol


import logging
logger = logging.getLogger("default")


def home(request, template_name='home.html'):
    context = {}
    return render_to_response(template_name, context, RequestContext(request))


def device_add(request, template_name='device_add.html'):
    request.session['device_id'] = None
    request.session['network_structure_id'] = None
    request.session['network_link_id'] = None
    request.session['protocol_id'] = None
    device_form = ShortDeviceForm()
    if request.method == 'POST':
        device_form = ShortDeviceForm(request.POST)
        if device_form.is_valid():
            device_instance = device_form.save()
            request.session['device_id'] = device_instance.id
            return HttpResponseRedirect(reverse('network_structure'))

    context = {
        'device_form': device_form,
    }
    return render_to_response(template_name, context, RequestContext(request))


def network_structure(request, template_name='network_structure.html'):
    network_structure_form = NetworkStructureForm()
    if request.method == 'POST':
        network_structure_form = NetworkStructureForm(request.POST)
        if network_structure_form.is_valid():
            request.session['network_structure_id'] = network_structure_form.cleaned_data['network_structure'].id
            return HttpResponseRedirect(reverse('network_link'))

    context = {
        'network_structure_form': network_structure_form,
    }
    return render_to_response(template_name, context, RequestContext(request))


def network_link(request, template_name='network_link.html'):
    network_link_form = NetworkLinkForm()
    if request.method == 'POST':
        network_link_form = NetworkLinkForm(request.POST)
        if network_link_form.is_valid():
            network_link_instance = network_link_form.save()
            request.session['network_link_id'] = network_link_instance.id
            return HttpResponseRedirect(reverse('protocol'))

    context = {
        'network_link_form': network_link_form,
    }
    return render_to_response(template_name, context, RequestContext(request))


def protocol(request, template_name='protocol.html'):
    protocol_form = ProtocolForm()
    if request.method == 'POST':
        protocol_form = ProtocolForm(request.POST)
        if protocol_form.is_valid():
            protocol_instance = protocol_form.save()
            request.session['protocol_id'] = protocol_instance.id
            return HttpResponseRedirect(reverse('payload'))

    context = {
        'protocol_form': protocol_form,
    }
    return render_to_response(template_name, context, RequestContext(request))


def payload(request, template_name='payload.html'):
    if request.method == 'POST':
        device_id = request.session.get('device_id', None)
        network_structure_id = request.session.get('network_structure_id', None)
        network_link_id = request.session.get('network_link_id', None)
        protocol_id = request.session.get('protocol_id', None)
        device = get_object_or_404(Device, id=device_id)
        device.network_structure = get_object_or_404(NetworkStructure, id=network_structure_id)
        device.network_link = get_object_or_404(NetworkLink, id=network_link_id)
        device.protocol = get_object_or_404(Protocol, id=protocol_id)
        device.save()
        return HttpResponseRedirect(reverse('device_config', args=(device_id,)))
    context = {
        'payload_form': {},
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
        'monthly_cost': calculate_cost(device_instance),
    }
    return render_to_response(template_name, context, RequestContext(request))

def calculate_cost(device):
    payload_size = 100000
    transmission_size = device.network_structure.transmission_size(payload_size, device.number, device.protocol.overhead, device.protocol.encryption_overhead)
    print transmission_size
    print device.frequency
    bytes_per_month = transmission_size * device.frequency
    real_bytes_per_month = device.frequency_factor(bytes_per_month)

    return (real_bytes_per_month / 100000) * device.network_link.cost_per_mb

def demo(request, template_name='demo.html'):
    context = {}
    return render_to_response(template_name, context, RequestContext(request))

