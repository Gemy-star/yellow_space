# Generated by Django 4.0.1 on 2022-02-11 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_rename_btn_text_homepage_btn_text_ar_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='show_section_background',
            field=models.ImageField(null=True, upload_to='backgrounds/'),
        ),
    ]
