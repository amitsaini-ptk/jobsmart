from django.shortcuts import render
from jobsopening.models import opening


def jopening(request):
	
	obj = opening.objects.all()
	
	return render(request,'copening.html', {'opening':obj})

def Home(request):

	return render(request,'Home.html')
	

from simple_search import search_filter
from .models import opening

query = 'test'
search_fields = ['^title', 'description', '=id']
f = search_filter(search_fields, query)
filtered = MyModel.objects.filter(f)

# Create your views here.
