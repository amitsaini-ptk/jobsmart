from django.db import models
from deligates.models import deligate


CONT_CHOICES= (('ASIA', 'ASIA'),('AUSTRALIA','AUSTRALIA'),('EUROPE','EUROPE'),('AFRICA','AFRICA'),('ANTARCTICA','ANTARCTICA'),('SOUTH AMERICA','SOUTH AMERICA'),('NORTH AMERICA','NORTH AMERICA') )

GENDER_CHOICES = (('Male', 'Male'),('Female', 'Female') )

CAND_CHOICES = (('FRESHER', 'FRESHER'),('EXPERIENCED', 'EXPERIENCED') )



DEPT_CHOICES=(('ADMIN', 'ADMIN'),('HUMAN RESOURCES', 'HUMAN RESOURCES'),('ACCOUNTS', 'ACCOUNTS'),('INFORMATION TECHNOLOGY', 'INFORMATION TECHNOLOGY'),('PURCHASE', 'PURCHASE'),('PRODUCTION', 'PRODUCTION'),('SALE & MKT', 'SALE & MKT'),('WHARE HOUSE', 'WHARE HOUSE'),('TIME OFFICE','TIME OFFICE'),('SECURITY', 'SECURITY'),('MAINTENANCE', 'MAINTENANCE'),('OTHERS', 'OTHERS') )

DESIG_CHOICES=(('CEO', 'CEO'),('GENERAL MANAGER', 'GENERAL MANAGER'),('HOD', 'HOD'),('DUTY MANAGER', 'DUTY MANAGER'),('MANAGER', 'MANAGER'),('ASST. MANAGER', 'ASST. MANAGER'),('EXECUTIVE', 'EXECUTIVE'),('OFFICER', 'OFFICER'),('TRAINEE', 'TRAINEE'),('OTHERS', 'OTHERS') )
EXP_CHOICES=(('FRESHER', 'FRESHER'),('0-2 YEARS', '0-2 YEARS'),('2-5 YEARS', '2-5 YEARS'),('5-7 YEARS', '5-7 YEARS'),('7-10', '7-10 YEARS'),('10-12 YEARS', '10-12 YEARS'),('12-15 YEARS', '12-15 YEARS'),('15-20 YEARS', '15-20 YEARS'),('20 YEARS', '20 YEARS') )


class hopening(models.Model):
	Deligate=models.ForeignKey(deligate,null=True,blank=True,on_delete=models.SET_NULL)

	Regno = models.CharField(default=0,max_length=100)
	Industry = models.CharField(default=0,max_length=100)
	Continent=models.CharField(default=0,choices=CONT_CHOICES,max_length=100)
	Country= models.CharField(default=0, max_length=100)
	Province=models.CharField(default=0,max_length=100)
	Department= models.CharField(default=0,choices=DEPT_CHOICES, max_length=50)
	Qualification=models.CharField(default=0,max_length=100)
	Designation = models.CharField(default=0,choices=DESIG_CHOICES, max_length=50)
	Ctype = models.CharField(default=0,choices=CAND_CHOICES, max_length=50)
	Gender = models.CharField(default=0,choices=GENDER_CHOICES, max_length=50)
	Minexp=models.CharField(default=0,choices=EXP_CHOICES, max_length=50)
	Budget = models.CharField(default=0,max_length=50)
	DetailJD  =models.TextField(default=0,)

# Create your models here.
