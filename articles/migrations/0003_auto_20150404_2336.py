# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20150404_2330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='additional_image',
            field=models.ImageField(upload_to='.'),
        ),
        migrations.AlterField(
            model_name='article',
            name='hero_image',
            field=models.ImageField(upload_to='.'),
        ),
    ]
