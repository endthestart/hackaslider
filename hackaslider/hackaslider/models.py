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
    """
    A class for the structure of the network
    - MESH
    - Single device
    - Gateway / Edge
    """
    name = models.CharField(
        _(u"name"),
        null=True,
        blank=True,
        max_length=255,
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

    def __unicode__(self):
        return u"{}".format(self.name)

    class Meta:
        ordering = ['name']
        verbose_name = _(u"network structure")
        verbose_name_plural = _(u"network structures")

    def save(self, **kwargs):
        if self.name and not self.slug:
            self.slug = slugify(self.name)

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
