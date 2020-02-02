# Generated by Django 2.2.6 on 2019-10-31 18:22

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, editable=False),
        ),
        migrations.AlterField(
            model_name='photo',
            name='user',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
