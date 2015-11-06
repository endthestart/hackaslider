from django import forms
from django.forms import ModelForm

from .models import Device, NetworkLink


class ShortDeviceForm(ModelForm):
    class Meta:
        model = Device
        fields = ['name', 'network_structure', 'frequency', 'frequency_category', 'number']


class DeviceForm(ModelForm):
    class Meta:
        model = Device
        fields = ['name', 'network_link', 'network_structure', 'protocol', 'frequency', 'frequency_category', 'number']


class NetworkLinkForm(ModelForm):
    class Meta:
        model = NetworkLink
        fields = ['name', 'network_type', 'description', 'cost_per_mb']