# Generated by Django 3.0.7 on 2020-07-10 07:12

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Title')),
                ('image', models.ImageField(upload_to='category_images', verbose_name='Image')),
                ('is_published', models.BooleanField(default=True, verbose_name='is published')),
                ('order', models.PositiveIntegerField(default=1, verbose_name='Order')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ('order',),
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Name')),
                ('email', models.EmailField(max_length=40, verbose_name='Email')),
                ('subject', models.CharField(max_length=255, verbose_name='Subject')),
                ('message', models.TextField(verbose_name='Message')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contacts',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, verbose_name='Title')),
                ('is_published', models.BooleanField(default=True, verbose_name='is published')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tag',
            },
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Basligi')),
                ('image', models.ImageField(upload_to='recipes', verbose_name='Sekil')),
                ('long_description', ckeditor.fields.RichTextField(verbose_name='Genis mezmunu')),
                ('slug', models.SlugField(editable=False, max_length=255, unique=True, verbose_name='slug')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_published', models.BooleanField(default=True, verbose_name='is published')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stories', to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stories', to='stories.Category', verbose_name='Kateqoriya')),
                ('tags', models.ManyToManyField(related_name='stories', to='stories.Tag', verbose_name='Tags')),
            ],
            options={
                'verbose_name': 'Hekaye',
                'verbose_name_plural': 'Hekayeler',
                'ordering': ('-created_at', '-title'),
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Basligi')),
                ('short_description', models.CharField(help_text='Bu sahe repestler siyahisinda reseptin mezmunu olaraq gorunur...', max_length=255, verbose_name='Qisa Mezmunu')),
                ('image', models.ImageField(upload_to='recipes', verbose_name='Sekil')),
                ('long_description', ckeditor.fields.RichTextField(verbose_name='Genis mezmunu')),
                ('show_home_page', models.BooleanField(default=False)),
                ('slug', models.SlugField(editable=False, max_length=255, unique=True, verbose_name='slug')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_published', models.BooleanField(default=True, verbose_name='is published')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipes', to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipes', to='stories.Category', verbose_name='Kateqoriya')),
                ('tags', models.ManyToManyField(related_name='recipes', to='stories.Tag', verbose_name='Tags')),
            ],
            options={
                'verbose_name': 'Resept',
                'verbose_name_plural': 'Reseptler',
                'ordering': ('-created_at', '-title'),
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Name')),
                ('email', models.EmailField(blank=True, max_length=40, null=True, verbose_name='Email')),
                ('message', models.TextField(verbose_name='Message')),
                ('parent_comment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child_comments', to='stories.Comment')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='stories.Recipe')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
