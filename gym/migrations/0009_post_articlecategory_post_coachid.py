# Generated by Django 4.1.4 on 2023-01-03 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coach', '0001_initial'),
        ('gym', '0008_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='articleCategory',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='coachId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='coach.coach'),
        ),
    ]
