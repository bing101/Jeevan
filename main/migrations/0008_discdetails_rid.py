# Generated by Django 2.1 on 2018-09-29 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_join'),
    ]

    operations = [
        migrations.AddField(
            model_name='discdetails',
            name='rid',
            field=models.IntegerField(default=1, max_length=10),
        ),
    ]
