# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_company_company_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='company_location',
        ),
        migrations.AddField(
            model_name='company',
            name='company_date_added',
            field=models.DateTimeField(default=datetime.date(2014, 9, 7), verbose_name=b'date added'),
            preserve_default=False,
        ),
    ]
