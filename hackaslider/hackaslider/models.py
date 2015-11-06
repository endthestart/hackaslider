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


class Protocol(models.Model):
    """
    A class for protocols
    - COAP
    - HTTP
    - RPC
    - WEB Sockets
    """
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
    type = models.CharField(
        _(u"type"),
        null=True,
        blank=True,
        max_length=255,
        choices=PROTOCOL_TYPE_CHOICES,
        default=HTTP,
        help_text=_(u"The type of the protocol."),
    )
    slug = models.SlugField(
        _(u"slug"),
        blank=True,
        help_text=_(u"Used for URLs, auto-generated from name if blank."),
        max_length=255,
    )
    description = models.TextField(
        _(u"description"),
        null=True,
        blank=True,
        help_text=_(u"This should be a more lengthy description of the protocol."),
    )
    encryption = models.BooleanField(
        _(u"active"),
        default=False,
        blank=True,
        help_text=_(u"Whether or not encryption will be used when transmitting data."),
    )

    @property
    def overhead(self):
        protocol_overhead = 0
        if self.type == self.COAP:
            protocol_overhead = 100000
        elif self.type == self.HTTP:
            protocol_overhead = 100000
        elif self.type == self.RPC:
            protocol_overhead = 200000
        elif self.type == self.SOCKETS:
            protocol_overhead = 150000
        return protocol_overhead

    @property
    def encryption_overhead(self):
        if self.encryption:
            return 100000
        else:
            return 0

    def __unicode__(self):
        return u"{}".format(self.type)

    class Meta:
        ordering = ['type']
        verbose_name = _(u"protocol")
        verbose_name_plural = _(u"protocols")

    def save(self, **kwargs):
        if self.type and not self.slug:
            self.slug = slugify(self.type)

        super(Protocol, self).save(**kwargs)


class NetworkStructure(models.Model):
    SINGLE = 'SINGLE'
    MESH = 'MESH'
    GATEWAY = 'GATEWAY'
    PROTOCOL_TYPE_CHOICES = (
        (SINGLE, 'Single Device'),
        (MESH, 'Mesh'),
        (GATEWAY, 'Gateway'),
    )
    type = models.CharField(
        _(u"type"),
        null=True,
        blank=True,
        max_length=255,
        choices=PROTOCOL_TYPE_CHOICES,
        default=SINGLE,
        help_text=_(u"The name of the network structure."),
    )
    slug = models.SlugField(
        _(u"slug"),
        blank=True,
        help_text=_(u"Used for URLs, auto-generated from name if blank."),
        max_length=255,
    )
    description = models.TextField(
        _(u"description"),
        null=True,
        blank=True,
        help_text=_(u"This should be a more lengthy description of the network structure."),
    )

    def transmission_size(self, payload_size, number_of_devices, protocol_overhead, encryption_overhead):
        ts = 0
        if self.type == self.SINGLE:
            ts = (payload_size + protocol_overhead + encryption_overhead) * number_of_devices
        elif self.type == self.MESH:
            ts = (payload_size * number_of_devices) + protocol_overhead + encryption_overhead
        elif self.type == self.GATEWAY:
            ts = (payload_size * number_of_devices) + protocol_overhead + encryption_overhead
        return int(ts)

    def __unicode__(self):
        return u"{}".format(self.type)

    class Meta:
        ordering = ['type']
        verbose_name = _(u"network structure")
        verbose_name_plural = _(u"network structures")

    def save(self, **kwargs):
        if self.type and not self.slug:
            self.slug = slugify(self.type)

        super(NetworkStructure, self).save(**kwargs)


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
    network_structure = models.ForeignKey(
        NetworkStructure,
        blank=True,
        null=True,
    )
    protocol = models.ForeignKey(
        Protocol,
        blank=True,
        null=True,
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

    def frequency_factor(self, bytes_per_month):
        if self.frequency_category == self.CONTROL:
            return bytes_per_month * 1
        elif self.frequency_category == self.MONITOR:
            return bytes_per_month * 0.5
        elif self.frequency_category == self.ALERT:
            return bytes_per_month * 0.1

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
