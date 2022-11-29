# Generated by Django 4.1.3 on 2022-11-29 11:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coach', '0006_remove_detail_coach'),
    ]

    operations = [
        migrations.AddField(
            model_name='detail',
            name='Coach',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='details', to='coach.coach'),
            preserve_default=False,
        ),
    ]