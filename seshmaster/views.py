from django.shortcuts import render
from django.http import HttpResponse
from seshmaster.forms import nightclub_form,signup_form
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
<<<<<<< HEAD
from seshmaster.forms import signup_form, UserProfileForm, NightclubUserImage
=======
from seshmaster.forms import signup_form, UserProfileForm
>>>>>>> e655d28cad41fab5061c8343832b51efc5071976

from django.contrib import auth
def index(request):


	return render(request, 'seshmaster/index.html')

def contact(request):
	
	
	return render(request, 'seshmaster/contact.html')
	
	
def signup(request):

        registered = False 

        if request.method == "POST":

                user_form = signup_form(data=request.POST)
                profile_form = UserProfileForm(data=request.POST)


                if user_form.is_valid() and profile_form.is_valid(): 

                        user = user_form.save()

                        user.set_password(user.password)
                        user.save()

                        profile = profile_form.save(commit=False)
                        profile.user = user

                        if 'picture' in request.FILES:
                                profile.picture = request.FILES['picture']

                        profile.save()
                        registered = True
                else: 
                        print(user_form.errors, profile_form.errors)
                
        else:
                user_form = signup_form()
                profile_form = UserProfileForm()

                

        return render(request, 'seshmaster/signup.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})
	
	
<<<<<<< HEAD
=======
	
def login(request):
	
	
	return render(request, 'seshmaster/login.html')
	
>>>>>>> e655d28cad41fab5061c8343832b51efc5071976
	
def nightclubbrowse(request):
	
	
	return render(request, 'seshmaster/nightclubbrowse.html')

	
def nightclubpage(request):
	
	
	return render(request, 'seshmaster/nightclubbrowse/nightclubpage.html')
	

def leavereview(request):
	
	
	return render(request, 'seshmaster/leavereview.html')
	

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
<<<<<<< HEAD
	
def user_login(request):

        if request.method == 'POST':

                username = request.POST.get('username')
                password = request.POST.get('password')

                user = authenticate(username=username, password=password)


                if user:
                        if user.is_active:

                                auth.login(request, user) 

                                return HttpResponseRedirect(reverse('index'))

                        else:
                                return HttpResponse("Your seshmaster account is inactive.")
                else:
                        print("Invalid login details: {0}, {1}".format(username, password))
                        return HttpResponse("Invalid login details supplied.")
        else:
                return render(request,"seshmaster/login.html",{})

def user_logout(request):

        auth.logout(request)
        return HttpResponseRedirect(reverse('index'))
		
def about(request):
	
	return render(request, 'seshmaster/about.html')
	
	
def addNCimage(request):
		form = NightclubUserImage

		if request.method == "POST":
				form= NightclubUserImage(request.POST)

				if form.is_valid():
					 form.save(commit=True)
					 return index(request)

				else:
					 print(form.errors)

        
		return render(request, 'seshmaster/addNCimage.html')
#def upload_image(request):
	
=======
	
def user_login(request):

        if request.method == 'POST':

                username = request.POST.get('username')
                password = request.POST.get('password')

                user = authenticate(username=username, password=password)


                if user:
                        if user.is_active:

                                auth.login(request, user) 

                                return HttpResponseRedirect(reverse('index'))

                        else:
                                return HttpResponse("Your seshmaster account is inactive.")
                else:
                        print("Invalid login details: {0}, {1}".format(username, password))
                        return HttpResponse("Invalid login details supplied.")
        else:
                return render(request,"seshmaster/login.html",{})

def user_logout(request):

        auth.logout(request)
        return HttpResponseRedirect(reverse('index'))
>>>>>>> e655d28cad41fab5061c8343832b51efc5071976

        


	
