# Generated by Django 3.0.7 on 2021-05-20 18:40

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('uploads', '0018_auto_20210520_1840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 20, 18, 40, 25, 896020, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='file',
            name='uploaded_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 20, 18, 40, 25, 895992, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='creationdate',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 20, 18, 40, 25, 893870, tzinfo=utc)),
        ),
    ]