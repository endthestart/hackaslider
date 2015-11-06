# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='The name of the device.', max_length=255, null=True, verbose_name='name', blank=True)),
                ('slug', models.SlugField(help_text='Used for URLs, auto-generated from name if blank.', max_length=255, verbose_name='slug', blank=True)),
                ('description', models.TextField(help_text='This should be a more lengthy description of the device.', null=True, verbose_name='description', blank=True)),
                ('cost_per_mb', models.DecimalField(decimal_places=2, max_digits=8, blank=True, help_text='The cost per MB for data transfer of the network.', null=True, verbose_name='cost per mb')),
                ('encryption', models.BooleanField(default=False, help_text='Whether or not encryption will be used when transmitting data.', verbose_name='active')),
                ('frequency', models.PositiveIntegerField(default=0, help_text='The number of seconds between data transmissions.', verbose_name='frequency')),
                ('frequency_category', models.CharField(default=b'MONITOR', choices=[(b'ALERT', b'Alert'), (b'CONTROL', b'Control'), (b'MONITOR', b'Monitor')], max_length=30, blank=True, help_text='The category of the frequency.', null=True, verbose_name='frequency category')),
                ('number', models.PositiveIntegerField(default=1, help_text='The number of devices in the network.', verbose_name='number')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'device',
                'verbose_name_plural': 'devices',
            },
        ),
        migrations.CreateModel(
            name='NetworkLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='The name of the network link.', max_length=255, null=True, verbose_name='name', blank=True)),
                ('slug', models.SlugField(help_text='Used for URLs, auto-generated from name if blank.', max_length=255, verbose_name='slug', blank=True)),
                ('description', models.TextField(help_text='This should be a more lengthy description of the network link.', null=True, verbose_name='description', blank=True)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'network link',
                'verbose_name_plural': 'network links',
            },
        ),
        migrations.CreateModel(
            name='NetworkStructure',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='The name of the network structure.', max_length=255, null=True, verbose_name='name', blank=True)),
                ('slug', models.SlugField(help_text='Used for URLs, auto-generated from name if blank.', max_length=255, verbose_name='slug', blank=True)),
                ('description', models.TextField(help_text='This should be a more lengthy description of the network structure.', null=True, verbose_name='description', blank=True)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'network structure',
                'verbose_name_plural': 'network structures',
            },
        ),
        migrations.CreateModel(
            name='Protocol',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='The name of the protocol.', max_length=255, null=True, verbose_name='name', blank=True)),
                ('slug', models.SlugField(help_text='Used for URLs, auto-generated from name if blank.', max_length=255, verbose_name='slug', blank=True)),
                ('description', models.TextField(help_text='This should be a more lengthy description of the protocol.', null=True, verbose_name='description', blank=True)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'protocol',
                'verbose_name_plural': 'protocols',
            },
        ),
        migrations.AddField(
            model_name='device',
            name='network_link',
            field=models.ForeignKey(blank=True, to='hackaslider.NetworkLink', null=True),
        ),
        migrations.AddField(
            model_name='device',
            name='network_structure',
            field=models.ForeignKey(blank=True, to='hackaslider.NetworkStructure', null=True),
        ),
        migrations.AddField(
            model_name='device',
            name='protocol',
            field=models.ForeignKey(blank=True, to='hackaslider.Protocol', null=True),
        ),
    ]
