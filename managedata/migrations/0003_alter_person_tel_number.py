# Generated by Django 4.0 on 2021-12-28 17:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managedata', '0002_alter_person_blood_type_alter_person_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='tel_number',
            field=models.CharField(max_length=15, null=True, unique=True, validators=[django.core.validators.RegexValidator(message="Tel Number must be entered in the format: '09012345678'. Up to 15 digits allowed.", regex='^[0-9]+$')], verbose_name='電話番号'),
        ),
    ]
