# Generated by Django 4.1.4 on 2022-12-18 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_remove_article_id_alter_article_writerid'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='isvalid',
            field=models.BooleanField(null=True),
        ),
    ]
