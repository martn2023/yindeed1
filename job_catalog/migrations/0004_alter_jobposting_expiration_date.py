# Generated by Django 5.0.3 on 2024-03-27 15:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_catalog', '0003_jobposting_organization_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobposting',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 25, 15, 11, 56, 839848, tzinfo=datetime.timezone.utc)),
        ),
    ]
