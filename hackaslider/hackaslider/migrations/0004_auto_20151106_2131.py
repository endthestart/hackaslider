# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackaslider', '0003_auto_20151106_2020'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='networkstructure',
            options={'ordering': ['type'], 'verbose_name': 'network structure', 'verbose_name_plural': 'network structures'},
        ),
        migrations.RemoveField(
            model_name='networkstructure',
            name='name',
        ),
        migrations.AddField(
            model_name='networkstructure',
            name='type',
            field=models.CharField(help_text='The name of the network structure.', max_length=255, null=True, verbose_name='type', blank=True),
        ),
    ]
