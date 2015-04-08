# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('publication_date', models.DateTimeField()),
                ('category', models.CharField(default='fk', choices=[('fk', 'Facebook'), ('go', 'Google'), ('apl', 'Apple'), ('micro', 'Microsoft')], max_length=5)),
                ('hero_image', models.ImageField(upload_to='hero_images')),
                ('additional_image', models.ImageField(upload_to='additional_image')),
                ('body_text', models.TextField()),
            ],
        ),
    ]
