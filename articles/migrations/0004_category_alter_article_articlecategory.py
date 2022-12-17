# Generated by Django 4.1.3 on 2022-12-12 01:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_alter_article_articlecategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.AlterField(
            model_name='article',
            name='articleCategory',
            field=models.ForeignKey(max_length=250, null=True, on_delete=django.db.models.deletion.CASCADE, to='articles.category'),
        ),
    ]
