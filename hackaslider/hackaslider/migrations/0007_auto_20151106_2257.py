# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackaslider', '0006_auto_20151106_2245'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='encryption',
            field=models.BooleanField(default=False, help_text='Whether or not encryption will be used when transmitting data.', verbose_name='active'),
        ),
        migrations.AlterField(
            model_name='device',
            name='protocol',
            field=models.CharField(default=b'HTTP', choices=[(b'COAP', b'COAP'), (b'HTTP', b'HTTP'), (b'RPC', b'RPC'), (b'SOCKETS', b'Web Sockets')], max_length=255, blank=True, help_text='The type of the protocol.', null=True, verbose_name='type'),
        ),
        migrations.DeleteModel(
            name='Protocol',
        ),
    ]
