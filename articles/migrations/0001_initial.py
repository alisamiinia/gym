# Generated by Django 4.1.4 on 2022-12-18 00:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


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
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('articleDescription', models.CharField(max_length=250)),
                ('articleContent', models.TextField()),
                ('readDuration', models.CharField(max_length=250)),
                ('PicUrl', models.TextField(null=True)),
                ('description', models.CharField(max_length=250, null=True)),
                ('writerName', models.CharField(max_length=250)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('articleCategory', models.ForeignKey(max_length=250, null=True, on_delete=django.db.models.deletion.CASCADE, to='articles.category')),
                ('writerid', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
