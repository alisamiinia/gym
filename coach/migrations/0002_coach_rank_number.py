# Generated by Django 4.1.3 on 2023-01-05 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coach', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coach',
            name='rank_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
