from django.shortcuts import render
from jobsopening.models import opening


def jopening(request):
	
	obj = opening.objects.all().order_by("-pk")
	
	return render(request,'copening.html', {'opening':obj})

def Home(request):

	return render(request,'Home.html')
	



# Create your views here.
