# Generated by Django 2.1 on 2018-09-18 15:44

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('visit', '0006_auto_20180918_0048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='activation_key',
            field=models.CharField(default=uuid.UUID('b74589fa-bb59-11e8-b452-9840bb29ab05'), max_length=64, verbose_name='Activation key'),
        ),
    ]