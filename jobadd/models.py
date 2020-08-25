from django.db import models

MODE_CHOICES = (('Online', 'Online'),('Website', 'Webite'),('Newspaper', 'Newspaper'),('Campus', 'Campus'))


class add(models.Model):
	Mode= models.CharField(default=0,choices=MODE_CHOICES,max_length=100)
	Date =models.DateTimeField()
	Img=models.ImageField(upload_to ='uploads/%Y/%m/%d/')
	Descrption=models.TextField(default=0,max_length=100)

	


# Create your models here.
