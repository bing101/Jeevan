# Generated by Django 2.1 on 2018-09-27 08:56

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('visit', '0010_auto_20180924_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='activation_key',
            field=models.CharField(default=uuid.UUID('2d6f0226-c233-11e8-abdc-9840bb29ab05'), max_length=64, verbose_name='Activation key'),
        ),
    ]