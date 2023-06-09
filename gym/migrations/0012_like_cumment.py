# Generated by Django 4.1.4 on 2023-01-03 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0011_rename_coachname_post_coachname'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isliked', models.BooleanField(default=False)),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gym.post')),
            ],
        ),
        migrations.CreateModel(
            name='Cumment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cumment', models.TextField()),
                ('writername', models.CharField(max_length=100)),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gym.post')),
            ],
        ),
    ]
