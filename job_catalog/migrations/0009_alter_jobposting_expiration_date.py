# Generated by Django 5.0.3 on 2024-04-01 10:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_catalog', '0008_alter_jobposting_expiration_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobposting',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 30, 10, 21, 27, 292076, tzinfo=datetime.timezone.utc)),
        ),
    ]
