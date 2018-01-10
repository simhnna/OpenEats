# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-10 09:43
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True, verbose_name='title')),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='title', unique=True, verbose_name='slug')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='author')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Cuisine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True, verbose_name='title')),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='title', unique=True, verbose_name='slug')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='author')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='title')),
                ('quantity', models.CharField(max_length=10, verbose_name='quantity')),
                ('measurement', models.CharField(blank=True, max_length=200, null=True, verbose_name='measurement')),
                ('preparation', models.CharField(blank=True, max_length=100, null=True, verbose_name='preparation')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Recipe Title')),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='title', unique=True, verbose_name='slug')),
                ('photo', models.ImageField(blank=True, upload_to='upload/recipe_photos', verbose_name='photo')),
                ('info', models.TextField(help_text='enter information about the recipe', verbose_name='info')),
                ('cook_time', models.IntegerField(help_text='enter time in minutes', verbose_name='cook time')),
                ('servings', models.IntegerField(help_text='enter total number of servings', verbose_name='servings')),
                ('directions', models.TextField(verbose_name='directions')),
                ('shared', models.IntegerField(choices=[(0, 'Share'), (1, 'Private')], default=0, help_text='share the recipe with the community or mark it private', verbose_name='shared')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='openeats.Course', verbose_name='course')),
                ('cuisine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='openeats.Cuisine', verbose_name='cuisine')),
            ],
            options={
                'ordering': ['pub_date', 'title'],
            },
        ),
        migrations.AddField(
            model_name='ingredient',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredients', to='openeats.Recipe', verbose_name='recipe'),
        ),
    ]
