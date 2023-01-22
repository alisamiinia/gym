# Generated by Django 4.1.4 on 2023-01-03 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='articleCategory',
            new_name='postCategoriesId',
        ),
        migrations.RemoveField(
            model_name='post',
            name='username',
        ),
        migrations.AlterField(
            model_name='post',
            name='comments',
            field=models.TextField(null=True),
        ),
    ]