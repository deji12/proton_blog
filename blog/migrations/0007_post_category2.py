# Generated by Django 4.0.2 on 2022-02-14 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_category2'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category2',
            field=models.CharField(default='Git', max_length=128),
        ),
    ]
