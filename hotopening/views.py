from django.shortcuts import render
from hotopening.models import hopening



def htopening(request):
	
	obj = hopening.objects.all()
	
	return render(request,'hotopening.html', {'opening':obj})
# Create your views here.
