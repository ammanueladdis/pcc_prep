# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0003_topic_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topic',
            old_name='user',
            new_name='owner',
        ),
    ]
