# Generated by Django 4.1.4 on 2023-01-03 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0012_like_cumment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='post',
        ),
        migrations.RemoveField(
            model_name='post',
            name='coachId',
        ),
        migrations.DeleteModel(
            name='Cumment',
        ),
        migrations.DeleteModel(
            name='Like',
        ),
        migrations.DeleteModel(
            name='post',
        ),
    ]