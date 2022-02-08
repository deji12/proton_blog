# Generated by Django 4.0.1 on 2022-02-08 11:23

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('title', models.CharField(max_length=10000000)),
                ('slug', models.SlugField(default='test')),
                ('body', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('image', models.ImageField(blank=True, null=True, upload_to='image/')),
                ('author_image', models.ImageField(blank=True, default='images/tpg.jpg', null=True, upload_to='author/')),
                ('category', models.CharField(default='Python', max_length=128)),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('num_clicks', models.IntegerField(default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
