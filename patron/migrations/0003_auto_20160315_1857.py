# Copyright 2016 Susan Bennett, David Mitchell, Jim Nicholls
#
# This file is part of AutoHolds.
#
# AutoHolds is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# AutoHolds is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with AutoHolds.  If not, see <http://www.gnu.org/licenses/>.
#
#  -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-15 18:57

from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patron', '0002_format_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='authority_record_number',
        ),
        migrations.AddField(
            model_name='author',
            name='friendly_name',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
