# Generated by Django 2.1 on 2018-09-17 18:40

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('visit', '0004_auto_20180918_0009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='activation_key',
            field=models.CharField(default=uuid.UUID('2b34fc2e-baa9-11e8-a1af-9840bb29ab05'), max_length=64, verbose_name='Activation key'),
        ),
    ]
