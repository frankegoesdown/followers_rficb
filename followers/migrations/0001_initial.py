# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
            ],
            options=None,
            bases=None,
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(verbose_name='Имя', max_length=32)),
            ],
            options={
                'ordering': ('name',),
            },
            bases=None,
        ),
        migrations.AddField(
            model_name='follow',
            name='follow_uid',
            field=models.ForeignKey(to='followers.Users', related_name='follow_uid'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='follow',
            name='uid',
            field=models.ForeignKey(to='followers.Users', related_name='uid'),
            preserve_default=True,
        ),
    ]
