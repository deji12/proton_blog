# Generated by Django 4.0.2 on 2022-02-14 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_category'),
    ]

    operations = [
        migrations.DeleteModel(
            name='category',
        ),
    ]
