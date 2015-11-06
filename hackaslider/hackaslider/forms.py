from django.forms import ModelForm

from .models import Device


class DeviceForm(ModelForm):
    class Meta:
        model = Device
        fields = ['name', 'network_link', 'network_structure', 'protocol', 'frequency', 'number']
