# Generated by Django 3.0 on 2020-08-19 04:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('deligates', '0002_auto_20200817_0029'),
        ('jobsopening', '0006_opening_regno'),
    ]

    operations = [
        migrations.AddField(
            model_name='opening',
            name='Deligate',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='deligates.deligate'),
        ),
    ]
