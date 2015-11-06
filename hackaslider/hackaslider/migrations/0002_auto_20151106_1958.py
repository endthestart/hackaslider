# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackaslider', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device',
            name='cost_per_mb',
        ),
        migrations.RemoveField(
            model_name='device',
            name='encryption',
        ),
        migrations.AddField(
            model_name='networklink',
            name='cost_per_mb',
            field=models.DecimalField(decimal_places=2, max_digits=8, blank=True, help_text='The cost per MB for data transfer of the network.', null=True, verbose_name='cost per mb'),
        ),
        migrations.AddField(
            model_name='networklink',
            name='network_type',
            field=models.CharField(default=b'ETHERNET', choices=[(b'ETHERNET', b'Ethernet or WiFi'), (b'CELLULAR', b'Cellular'), (b'SATELLITE', b'Satellite')], max_length=255, blank=True, help_text='The type of the network link.', null=True, verbose_name='network type'),
        ),
        migrations.AddField(
            model_name='protocol',
            name='encryption',
            field=models.BooleanField(default=False, help_text='Whether or not encryption will be used when transmitting data.', verbose_name='active'),
        ),
    ]
