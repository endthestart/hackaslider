# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackaslider', '0002_auto_20151106_1958'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='protocol',
            options={'ordering': ['type'], 'verbose_name': 'protocol', 'verbose_name_plural': 'protocols'},
        ),
        migrations.RemoveField(
            model_name='protocol',
            name='name',
        ),
        migrations.AddField(
            model_name='protocol',
            name='type',
            field=models.CharField(default=b'HTTP', choices=[(b'COAP', b'COAP'), (b'HTTP', b'HTTP'), (b'RPC', b'RPC'), (b'SOCKETS', b'Web Sockets')], max_length=255, blank=True, help_text='The type of the protocol.', null=True, verbose_name='type'),
        ),
        migrations.AlterField(
            model_name='device',
            name='frequency',
            field=models.PositiveIntegerField(default=1, help_text='The number of seconds between data transmissions.', verbose_name='frequency'),
        ),
    ]
