from django.shortcuts import render

from deligates.models import deligate


def jdeligate(request):
	
	obj = deligate.objects.all()
	
	return render(request,'deligate.html', {'deligate':obj})

# Create your views here.
