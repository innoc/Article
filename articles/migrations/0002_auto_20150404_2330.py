# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='additional_image',
            field=models.ImageField(upload_to='image'),
        ),
        migrations.AlterField(
            model_name='article',
            name='hero_image',
            field=models.ImageField(upload_to='image'),
        ),
    ]
