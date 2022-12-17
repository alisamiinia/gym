# Generated by Django 4.1.3 on 2022-12-11 23:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coach', '0001_initial'),
        ('gym', '0002_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('custoer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='coach.coach')),
                ('gym', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gym.gym')),
            ],
        ),
    ]