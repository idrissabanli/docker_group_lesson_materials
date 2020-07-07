# Generated by Django 3.0.7 on 2020-07-07 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0011_recipe_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='slug',
            field=models.SlugField(editable=False, unique=True, verbose_name='slug'),
        ),
    ]
