# Generated by Django 2.2.3 on 2019-07-24 19:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs_api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='owner',
        ),
    ]
