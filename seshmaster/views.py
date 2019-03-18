from django.shortcuts import render
from django.http import HttpResponse
from seshmaster.forms import nightclub_form,signup_form 

def index(request):


	return render(request, 'seshmaster/index.html')

def contact(request):
	
	
	return render(request, 'seshmaster/contact.html')
	
	
def signup(request):

        form = signup_form

        if request.method == "POST":
                form= signup_form(request.POST)

                if form.is_valid():
                        form.save(commit=True)
                        return index(request)

                else:
                        print(form.errors)

        return render(request, 'seshmaster/signup.html',{'form': form})
	
	
	
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
	
	
def addlocation(request):

        form = nightclub_form

        if request.method == "POST":
                form= nightclub_form(request.POST)

                if form.is_valid():
                        form.save(commit=True)
                        return index(request)

                else:
                        print(form.errors)

        return render(request, 'seshmaster/addlocations.html',{'form': form})
	
	
	
