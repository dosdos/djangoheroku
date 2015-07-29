# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import utilities.validators


class Migration(migrations.Migration):

    dependencies = [
        ('frontoffice', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='address',
            field=models.CharField(max_length=500, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='has_accepted_terms_and_conditions',
            field=models.BooleanField(default=False, validators=[utilities.validators.is_true]),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='image_url',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='is_email_verified',
            field=models.BooleanField(default=False),
        ),
    ]
