# Generated by Django 4.0.1 on 2022-02-18 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furniture', '0010_woodinformation_publication_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='woodinformation',
            name='publication_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]