# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_class_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='course',
            field=models.ForeignKey(to='courses.Course'),
        ),
    ]
