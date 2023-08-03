# Generated by Django 4.2 on 2023-06-04 13:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("jobwebsite", "0008_alter_profile_birthdate"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="age",
            field=models.PositiveIntegerField(
                default=18,
                validators=[
                    django.core.validators.MinValueValidator(16),
                    django.core.validators.MaxValueValidator(100),
                ],
            ),
        ),
    ]