from django.shortcuts import render

def jobadd(request):
	
	obj = add.objects.all()
	
	return render(request,'jobfest.html', {'add':obj})
# Create your views here.


# Create your views here.
