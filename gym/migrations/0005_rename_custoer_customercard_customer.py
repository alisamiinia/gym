# Generated by Django 4.1.4 on 2022-12-15 07:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0004_merge_20221215_1045'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customercard',
            old_name='custoer',
            new_name='customer',
        ),
    ]
