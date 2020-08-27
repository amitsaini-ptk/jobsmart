from django.shortcuts import render

from jobadd.models import add

def jobadd(request):
	
	obj = add.objects.all().order_by("-pk")
	
	return render(request,'jobadd.html', {'jobadd':obj})
# Create your views here.


# Create your views here.
