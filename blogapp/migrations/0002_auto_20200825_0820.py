# Generated by Django 3.1 on 2020-08-25 02:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 25, 2, 50, 33, 863149, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.TextField(),
        ),
    ]
