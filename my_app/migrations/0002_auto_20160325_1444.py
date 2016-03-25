# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='participant',
            name='rm_1',
        ),
        migrations.AddField(
            model_name='room',
            name='test_taker',
            field=models.ForeignKey(default=2, to='my_app.Participant'),
            preserve_default=False,
        ),
    ]
