# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('files_widget', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileicon',
            name='overlay_text',
            field=models.CharField(blank=True, max_length=7, null=True, help_text='Leave blank to display file extension'),
        ),
        migrations.AlterField(
            model_name='iconset',
            name='css_path',
            field=models.CharField(blank=True, max_length=200, null=True, help_text='Optional css file for icon styling'),
        ),
    ]
