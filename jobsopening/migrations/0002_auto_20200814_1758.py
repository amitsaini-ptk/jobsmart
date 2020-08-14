# Generated by Django 3.0 on 2020-08-14 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobsopening', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='opening',
            name='Qualification',
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AlterField(
            model_name='opening',
            name='State',
            field=models.CharField(choices=[('Andhra Pradesh', 'Andhra Pradesh'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Assam', 'Assam'), ('Bihar', 'Bihar'), ('Chandigarh', 'Chandigarh'), ('Chhattisgarh', 'Chhattisgarh'), ('Delhi', 'Delhi'), ('Goa', 'Goa'), ('Gujarat', 'Gujarat'), ('Haryana', 'Haryana'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Jammu & Kashmir', 'Jammu & Kashmir'), ('Jharkhand', 'Jharkhand'), ('Karnataka', 'Karnataka'), ('Kerala', 'Kerala'), ('Madhya Pradesh', 'Madhya Pradesh'), ('Maharashtra', 'Maharashtra'), ('Manipur', 'Manipur'), ('Meghalaya', 'Meghalaya'), ('Mizoram', 'Mizoram'), ('Nagaland', 'Nagaland'), ('Orissa', 'Orissa'), ('Puducherry', 'Puducherry'), ('Punjab', 'Punjab'), ('Rajasthan', 'Rajasthan'), ('Sikkim', 'Sikkim'), ('Uttar Pradesh', 'Uttar Pradesh'), ('Tamil Naidu', 'Tamil Naidu')], default=0, max_length=100),
        ),
    ]