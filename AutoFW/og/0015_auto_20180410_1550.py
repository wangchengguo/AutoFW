# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AutoFW', '0014_auto_20180410_1548'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='batch_report',
            name='API_name',
        ),
        migrations.RemoveField(
            model_name='batch_report',
            name='execute_log',
        ),
    ]
