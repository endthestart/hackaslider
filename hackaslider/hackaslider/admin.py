from django.contrib import admin
from .models import Device, NetworkLink, NetworkStructure, Protocol


admin.site.register(Device)
admin.site.register(NetworkLink)
admin.site.register(NetworkStructure)
admin.site.register(Protocol)
