from django.shortcuts import render
from django.http import HttpResponse

def index(request):


	return render(request, 'seshmaster/index.html')

def contact(request):
	
	
	return render(request, 'seshmaster/contact.html')
	
	
def signup(request):
	
	
	return render(request, 'seshmaster/signup.html')
	
	
def login(request):
	
	
	return render(request, 'seshmaster/login.html')
	
	
def nightclubbrowse(request):
	
	
	return render(request, 'seshmaster/nightclubbrowse.html')

	
def nightclubpage(request):
	
	
	return render(request, 'seshmaster/nightclubbrowse/nightclubpage.html')
	

def leavereview(request):
	
	
	return render(request, 'seshmaster/nightclubbrowse/leavereview.html')
	

def rateimage(request):
	
	
	return render(request, 'seshmaster/nightclubbrowse/rateimage.html')
	

def myaccount(request):
	
	
	return render(request, 'seshmaster/myaccount.html')
	
	
def myreviews(request):
	
	
	return render(request, 'seshmaster/myaccount/myreviews.html')
	
	
def mynightclubs(request):
	
	
	return render(request, 'seshmaster/mynightclubs.html')
	
	
	