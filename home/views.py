from django.shortcuts import render

# Create your views here.

def home(request):
	"""
	主页
	"""
	return render(request, 'home/home.html')