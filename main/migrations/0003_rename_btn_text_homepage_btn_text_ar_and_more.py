# Generated by Django 4.0.1 on 2022-02-11 16:36

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homepage',
            old_name='btn_text',
            new_name='btn_text_ar',
        ),
        migrations.RenameField(
            model_name='homepage',
            old_name='btn_url',
            new_name='btn_text_en',
        ),
        migrations.RenameField(
            model_name='homepage',
            old_name='category_description',
            new_name='category_description_ar',
        ),
        migrations.RenameField(
            model_name='homepage',
            old_name='description',
            new_name='category_description_en',
        ),
        migrations.RenameField(
            model_name='homepage',
            old_name='category_title',
            new_name='category_title_ar',
        ),
        migrations.RenameField(
            model_name='homepage',
            old_name='furniture_title',
            new_name='category_title_en',
        ),
        migrations.RenameField(
            model_name='homepage',
            old_name='furniture_description',
            new_name='description_ar',
        ),
        migrations.RenameField(
            model_name='homepage',
            old_name='header',
            new_name='description_en',
        ),
        migrations.RenameField(
            model_name='homepage',
            old_name='subheader',
            new_name='furniture_title_ar',
        ),
        migrations.AddField(
            model_name='homepage',
            name='furniture_description_ar',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='furniture_description_en',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='furniture_title_en',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='header_ar',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='header_en',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='homepage_background',
            field=models.ImageField(null=True, upload_to='backgrounds/'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='subheader_ar',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='subheader_en',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
