# Generated by Django 5.0.6 on 2024-07-03 10:48

import pathlib
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cook_house', '0002_alter_recipe_preview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='preview',
            field=models.ImageField(default=None, null=True, upload_to=pathlib.PureWindowsPath('C:/reps/gb_recipies/root_prj/uploads')),
        ),
    ]