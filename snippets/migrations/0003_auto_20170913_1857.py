# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0002_auto_20170913_1855'),
    ]

    operations = [
        migrations.RenameField(
            model_name='summary',
            old_name='negative',
            new_name='output',
        ),
        migrations.RemoveField(
            model_name='summary',
            name='positive',
        ),
    ]
