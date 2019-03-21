from django.shortcuts import render
from django.http import HttpResponse
from seshmaster.forms import nightclub_form,signup_form
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from seshmaster.forms import signup_form, UserProfileForm,ReviewForm
from seshmaster.models import Nightclub
from seshmaster.models import UserProfile
from seshmaster.models import Image
from django.contrib import auth
from django.contrib.auth.models import User
from django.db.models import Q

def index(request):

        club_list = Nightclub.objects.order_by('-average_score')[:3] 
        context_dict = {'spots': club_list}
        
                
        return render(request, 'seshmaster/index.html',context_dict)

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
	
	
	
def about(request):

        return render(request, "seshmaster/about.html")

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

def review(request):

        form = ReviewForm

        if request.method == "POST":
                form= ReviewForm(request.POST)

                if form.is_valid():
                        form.save(commit=True)
                        return index(request)

                else:
                        print(form.errors)

        return render(request, 'seshmaster/review.html',{'form': form})
	
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

def search(request):

        if request.method == "GET":

                query = request.GET.get("q")
                submitbutton = request.GET.get("submit")

                if query is not None:

                        lookups= Q(name__icontains=query)| Q(average_score__icontains=query)
                        results= Nightclub.objects.filter(lookups).distinct()
                        context={"results":results,"submitbutton":submitbutton}

                        return render(request,"seshmaster/search.html",context)
                else:
                        return render(request, "seshmaster/search.html")

        else:
                return render(request,"seshmaster/search.html")


def search_img(request):

        img_list = Image.objects.all()
        context_dict = {'imgs': img_list}
       

        return render(request,"seshmaster/images.html",context_dict)

               
