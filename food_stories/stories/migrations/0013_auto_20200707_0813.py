# Generated by Django 3.0.7 on 2020-07-07 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0012_auto_20200707_0802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='slug',
            field=models.SlugField(editable=False, max_length=255, unique=True, verbose_name='slug'),
        ),
    ]
