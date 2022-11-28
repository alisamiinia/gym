# Generated by Django 4.1.3 on 2022-11-28 22:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('coach', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Gym',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('adress', models.CharField(max_length=100)),
                ('phone', models.IntegerField()),
                ('gym_reg_code', models.IntegerField(default=999)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('time', models.CharField(default='8_22', max_length=30)),
                ('gym', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gym.gym')),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accepted', models.CharField(default='no', max_length=10)),
                ('coach', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='coach.coach')),
                ('gym', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gym.gym')),
            ],
        ),
    ]
