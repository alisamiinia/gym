# Generated by Django 4.1.4 on 2022-12-18 00:09

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('phone', models.CharField(max_length=11, validators=[django.core.validators.RegexValidator(regex='09(0[1-2])|(1[0-9])|(3[0-9])|(2[0-1])-?[0-9]{3}-?[0-9]{4}')])),
                ('age', models.IntegerField(blank=True, null=True)),
                ('height', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail', models.CharField(max_length=100)),
                ('Coach', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coach.coach')),
            ],
        ),
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('achievement', models.CharField(max_length=100)),
                ('year', models.CharField(max_length=11)),
                ('Coach', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coach.coach')),
            ],
        ),
    ]
