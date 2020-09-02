from django.db import models

STATE_CHOICES=(('Andhra Pradesh', 'Andhra Pradesh'),('Arunachal Pradesh', 'Arunachal Pradesh'),('Assam', 'Assam'),('Bihar', 'Bihar'),('Chandigarh', 'Chandigarh'),('Chhattisgarh', 'Chhattisgarh'),('Delhi', 'Delhi'),('Goa','Goa'),('Gujarat','Gujarat'),('Haryana','Haryana'),('Himachal Pradesh', 'Himachal Pradesh'),('Jammu & Kashmir', 'Jammu & Kashmir'),('Jharkhand', 'Jharkhand'),('Karnataka', 'Karnataka'),('Kerala', 'Kerala'),('Madhya Pradesh', 'Madhya Pradesh'),('Maharashtra', 'Maharashtra'),('Manipur','Manipur'),('Meghalaya','Meghalaya'),('Mizoram','Mizoram'),('Nagaland','Nagaland'),('Orissa', 'Orissa'),('Puducherry','Puducherry'),('Punjab','Punjab'),('Rajasthan','Rajasthan'),('Sikkim','Sikkim'),('Uttar Pradesh','Uttar Pradesh'),('Tamil Naidu','Tamil Naidu'))

class deligate(models.Model):
	Regno= models.CharField(default=0,max_length=100)
	Name=models.CharField(default=0,max_length=100)
	Address=models.TextField(default=0,max_length=255)
	City=models.CharField(default=0,max_length=100)
	Pincode=models.IntegerField()
	State= models.CharField(default=0,choices=STATE_CHOICES, max_length=100)
	Mobno= models.CharField(default=0,max_length=15)
	Mailid=models.CharField(default=0,max_length=100)
	
	
# Create your models here.
