from django import forms
from django.forms import ModelForm

from .models import Device, NetworkStructure, NetworkLink, Protocol


class ShortDeviceForm(ModelForm):
    class Meta:
        model = Device
        fields = ['name', 'frequency', 'frequency_category', 'number']


class DeviceForm(ModelForm):
    class Meta:
        model = Device
        fields = ['name', 'network_link', 'network_structure', 'protocol', 'frequency', 'number']


class NetworkStructureForm(forms.Form):
    network_structure = forms.ModelChoiceField(queryset=NetworkStructure.objects.all())


class NetworkLinkForm(ModelForm):
    class Meta:
        model = NetworkLink
        fields = ['name', 'network_type', 'description', 'cost_per_mb']


class ProtocolForm(ModelForm):
    class Meta:
        model = Protocol
        fields = ['type', 'encryption']