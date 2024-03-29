# Generated by Django 4.2.9 on 2024-01-23 14:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_ckeditor_5.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('body', django_ckeditor_5.fields.CKEditor5Field(verbose_name='Text')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(default=0, verbose_name=((0, 'Draft'), (1, 'Publish')))),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]
