# Generated by Django 4.1.3 on 2022-11-28 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='Gym',
            new_name='gym',
        ),
    ]
