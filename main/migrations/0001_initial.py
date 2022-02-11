# Generated by Django 4.0.1 on 2022-01-28 16:31

import ckeditor.fields
import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Homepage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', ckeditor.fields.RichTextField(null=True)),
                ('subheader', models.CharField(blank=True, max_length=255, null=True)),
                ('btn_text', models.CharField(blank=True, max_length=255, null=True)),
                ('btn_url', models.CharField(blank=True, max_length=255, null=True)),
                ('btn_color', colorfield.fields.ColorField(default='#FFFFFF', image_field=None, max_length=18, samples=None)),
                ('description', ckeditor.fields.RichTextField(null=True)),
                ('category_title', models.CharField(blank=True, max_length=255, null=True)),
                ('category_description', ckeditor.fields.RichTextField(null=True)),
                ('furniture_title', models.CharField(blank=True, max_length=255, null=True)),
                ('furniture_description', ckeditor.fields.RichTextField(null=True)),
                ('mobile', models.CharField(max_length=20)),
                ('other_phone', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('facebook_link', models.URLField(blank=True, null=True)),
                ('instagram_link', models.URLField(blank=True, null=True)),
                ('youtube_link', models.URLField(blank=True, null=True)),
                ('twitter_link', models.URLField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
