# Generated by Django 3.0 on 2020-09-02 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deligates', '0002_auto_20200817_0029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deligate',
            name='Mobno',
            field=models.CharField(default=0, max_length=15),
        ),
    ]
