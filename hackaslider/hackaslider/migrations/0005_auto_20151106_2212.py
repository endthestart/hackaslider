# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackaslider', '0004_auto_20151106_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='networkstructure',
            name='type',
            field=models.CharField(default=b'SINGLE', choices=[(b'SINGLE', b'Single Device'), (b'MESH', b'Mesh'), (b'GATEWAY', b'Gateway')], max_length=255, blank=True, help_text='The name of the network structure.', null=True, verbose_name='type'),
        ),
    ]
