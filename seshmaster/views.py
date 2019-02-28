from django.shortcuts import render
from django.http import HttpResponse

def home(request):


	return render(request, 'seshmaster/home.html', context=context_dict)

def contact(request):
	
	
	return render(request, 'seshmaster/contact.html', context=context_dict)
	
	
def signup(request):
	
	
	return render(request, 'seshmaster/signup.html', context=context_dict)
	
	
def login(request):
	
	
	return render(request, 'seshmaster/login.html', context=context_dict)
	
	
def nightclubbrowse(request):
	
	
	return render(request, 'seshmaster/nightclubbrowse.html', context=context_dict)

	
def nightclubpage(request):
	
	
	return render(request, 'seshmaster/nightclubbrowse/nightclubpage.html', context=context_dict)
	

def leavereview(request):
	
	
	return render(request, 'seshmaster/nightclubbrowse/leavereview.html', context=context_dict)
	

def rateimage(request):
	
	
	return render(request, 'seshmaster/nightclubbrowse/rateimage.html', context=context_dict)
	

def myaccount(request):
	
	
	return render(request, 'seshmaster/myaccount.html', context=context_dict)
	
	
def myreviews(request):
	
	
	return render(request, 'seshmaster/myaccount/myreviews.html', context=context_dict)
	
	
def mynightclubs(request):
	
	
	return render(request, 'seshmaster/mynightclubs.html', context=context_dict)
	
	
	