# Generated by Django 4.0.1 on 2022-01-28 15:15

from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(db_index=True, editable=False, verbose_name='order')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='name')),
                ('picture', models.ImageField(upload_to='category/')),
            ],
            options={
                'ordering': ('order',),
                'abstract': False,
            },
        ),
    ]
