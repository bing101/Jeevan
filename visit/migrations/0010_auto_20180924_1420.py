# Generated by Django 2.1 on 2018-09-24 08:50

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('visit', '0009_auto_20180919_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='activation_key',
            field=models.CharField(default=uuid.UUID('d79a6cc0-bfd6-11e8-bb2a-9840bb29ab05'), max_length=64, verbose_name='Activation key'),
        ),
    ]