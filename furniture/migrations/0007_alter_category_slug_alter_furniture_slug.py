# Generated by Django 4.0.1 on 2022-02-11 19:06

from django.db import migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('furniture', '0006_rename_description_1_furniture_description_1_ar_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='name_en'),
        ),
        migrations.AlterField(
            model_name='furniture',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='name_en'),
        ),
    ]