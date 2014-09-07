# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20140905_0027'),
    ]

    operations = [
        migrations.AddField(
            model_name='salary',
            name='salary_date',
            field=models.DateTimeField(default=datetime.date(2014, 9, 5), verbose_name=b'date published'),
            preserve_default=False,
        ),
    ]
