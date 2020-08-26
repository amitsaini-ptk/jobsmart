# Generated by Django 3.0 on 2020-08-25 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='add',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Mode', models.CharField(choices=[('Online', 'Online'), ('Website', 'Webite'), ('Newspaper', 'Newspaper'), ('Campus', 'Campus')], default=0, max_length=100)),
                ('Date', models.DateTimeField()),
                ('img', models.ImageField(upload_to='uploads/%Y/%m/%d/')),
                ('Descrption', models.TextField(default=0, max_length=100)),
            ],
        ),
    ]