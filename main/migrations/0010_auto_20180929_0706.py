# Generated by Django 2.1 on 2018-09-29 01:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_discover_rid2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='discdetails',
            name='rid',
        ),
        migrations.RemoveField(
            model_name='discover',
            name='rid2',
        ),
    ]
