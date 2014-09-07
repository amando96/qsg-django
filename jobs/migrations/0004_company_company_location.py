# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_salary_salary_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='company_location',
            field=models.ForeignKey(default=0, to='jobs.District'),
            preserve_default=True,
        ),
    ]
