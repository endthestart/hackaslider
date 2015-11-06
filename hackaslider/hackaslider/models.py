from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext_lazy as _


class NetworkLink(models.Model):
    """
    A class for network link
    - Ethernet
    - Cellular
    - Satellite
    """
    ETHERNET = 'ETHERNET'
    CELLULAR = 'CELLULAR'
    SATELLITE = 'SATELLITE'
    NETWORK_TYPE_CHOICES = (
        (ETHERNET, 'Ethernet or WiFi'),
        (CELLULAR, 'Cellular'),
        (SATELLITE, 'Satellite'),
    )
    name = models.CharField(
        _(u"name"),
        null=True,
        blank=True,
        max_length=255,
        help_text=_(u"The name of the network link."),
    )
    network_type = models.CharField(
        _(u"network type"),
        null=True,
        blank=True,
        max_length=255,
        choices=NETWORK_TYPE_CHOICES,
        default=ETHERNET,
        help_text=_(u"The type of the network link."),
    )
    slug = models.SlugField(
        _(u"slug"),
        blank=True,
        max_length=255,
        help_text=_(u"Used for URLs, auto-generated from name if blank."),
    )
    description = models.TextField(
        _(u"description"),
        null=True,
        blank=True,
        help_text=_(u"This should be a more lengthy description of the network link."),
    )
    cost_per_mb = models.DecimalField(
        _(u"cost per mb"),
        max_digits=8,
        decimal_places=2,
        null=True,
        blank=True,
        help_text=_(u"The cost per MB for data transfer of the network."),
    )

    def __unicode__(self):
        return u"{}".format(self.name)

    class Meta:
        ordering = ['name']
        verbose_name = _(u"network link")
        verbose_name_plural = _(u"network links")

    def save(self, **kwargs):
        if self.name and not self.slug:
            self.slug = slugify(self.name)

        super(NetworkLink, self).save(**kwargs)


class Device(models.Model):
    """
    A class for the device configuration

    Ability to create a device and apply the network type and attributes.
    """
    ALERT = 'ALERT'
    CONTROL = 'CONTROL'
    MONITOR = 'MONITOR'
    FREQUENCY_CATEGORY_CHOICES = (
        (ALERT, 'Alert'),
        (CONTROL, 'Control'),
        (MONITOR, 'Monitor'),
    )

    SINGLE = 'SINGLE'
    MESH = 'MESH'
    GATEWAY = 'GATEWAY'
    NETWORK_STRUCTURE_CHOICES = (
        (SINGLE, 'Single Device'),
        (MESH, 'Mesh'),
        (GATEWAY, 'Gateway'),
    )
    COAP = 'COAP'
    HTTP = 'HTTP'
    RPC = 'RPC'
    SOCKETS = 'SOCKETS'
    PROTOCOL_TYPE_CHOICES = (
        (COAP, 'COAP'),
        (HTTP, 'HTTP'),
        (RPC, 'RPC'),
        (SOCKETS, 'Web Sockets'),
    )
    name = models.CharField(
        _(u"name"),
        null=True,
        blank=True,
        max_length=255,
        help_text=_(u"The name of the device."),
    )
    slug = models.SlugField(
        _(u"slug"),
        blank=True,
        max_length=255,
        help_text=_(u"Used for URLs, auto-generated from name if blank."),
    )
    description = models.TextField(
        _(u"description"),
        null=True,
        blank=True,
        help_text=_(u"This should be a more lengthy description of the device."),
    )
    network_link = models.ForeignKey(
        NetworkLink,
        blank=True,
        null=True,
    )
    network_structure = models.CharField(
        _(u"type"),
        null=True,
        blank=True,
        max_length=255,
        choices=NETWORK_STRUCTURE_CHOICES,
        default=SINGLE,
        help_text=_(u"The name of the network structure."),
    )
    protocol = models.CharField(
        _(u"type"),
        null=True,
        blank=True,
        max_length=255,
        choices=PROTOCOL_TYPE_CHOICES,
        default=HTTP,
        help_text=_(u"The type of the protocol."),
    )
    frequency = models.PositiveIntegerField(
        _(u"frequency"),
        default=1,
        help_text=_(u"The number of seconds between data transmissions."),
    )
    frequency_category = models.CharField(
        _(u"frequency category"),
        null=True,
        blank=True,
        max_length=30,
        choices=FREQUENCY_CATEGORY_CHOICES,
        default=MONITOR,
        help_text=_(u"The category of the frequency.")
    )
    number = models.PositiveIntegerField(
        _(u"number"),
        default=1,
        help_text=_(u"The number of devices in the network."),
    )
    encryption = models.BooleanField(
        _(u"active"),
        default=False,
        blank=True,
        help_text=_(u"Whether or not encryption will be used when transmitting data."),
    )

    def transmission_size(self, payload_size):
        ts = 0
        if self.network_structure == self.SINGLE:
            ts = (payload_size + self.protocol_overhead + self.encryption_overhead) * self.number
        elif self.network_structure == self.MESH:
            ts = (payload_size * self.number) + self.protocol_overhead + self.encryption_overhead
        elif self.network_structure == self.GATEWAY:
            ts = (payload_size * self.number) + self.protocol_overhead + self.encryption_overhead
        return int(ts)

    def frequency_factor(self, bytes_per_month):
        if self.frequency_category == self.CONTROL:
            return int(bytes_per_month * 1)
        elif self.frequency_category == self.MONITOR:
            return int(bytes_per_month * 0.5)
        elif self.frequency_category == self.ALERT:
            return int(bytes_per_month * 0.1)

    @property
    def protocol_overhead(self):
        protocol_overhead = 0
        if self.protocol == self.COAP:
            protocol_overhead = 20
        elif self.protocol == self.HTTP:
            protocol_overhead = 1200
        elif self.protocol == self.RPC:
            protocol_overhead = 1350
        elif self.protocol == self.SOCKETS:
            protocol_overhead = 1100
        return protocol_overhead

    @property
    def encryption_overhead(self):
        if self.encryption:
            return 5000
        else:
            return 0

    def __unicode__(self):
        return u"{}".format(self.name)

    class Meta:
        ordering = ['name']
        verbose_name = _(u"device")
        verbose_name_plural = _(u"devices")

    def save(self, **kwargs):
        if self.name and not self.slug:
            self.slug = slugify(self.name)

        super(Device, self).save(**kwargs)
