# Generated by Django 4.0.1 on 2022-02-11 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furniture', '0004_woodinformation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='name',
            new_name='name_ar',
        ),
        migrations.AddField(
            model_name='category',
            name='name_en',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]