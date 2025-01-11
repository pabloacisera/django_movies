from django.shortcuts import render

# Create your views here.
def homeView(request):
	# el home.html esta en la carpeta templates
	return render(request, 'home.html')