# Generated by Django 3.0.7 on 2020-12-17 19:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('uploads', '0012_auto_20201217_1917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 17, 19, 17, 23, 456734, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='file',
            name='uploaded_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 17, 19, 17, 23, 456708, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='creationdate',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 17, 19, 17, 23, 454665, tzinfo=utc)),
        ),
    ]
