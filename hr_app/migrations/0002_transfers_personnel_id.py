# Generated by Django 3.2.11 on 2022-07-12 05:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hr_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transfers',
            name='personnel_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='hr_app.personnelmasters'),
        ),
    ]
