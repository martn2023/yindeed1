# Generated by Django 5.0.3 on 2024-04-01 10:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job_applications', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobapplication',
            old_name='application_email',
            new_name='email_address',
        ),
    ]