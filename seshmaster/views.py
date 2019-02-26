from django.shortcuts import render
from django.http import HttpResponse


def index(request):

    context_dict = {'boldmessage': "hey!"}

    return render(request,'seshmaster/index.html', context=context_dict)


def about(request):
    return HttpResponse("About Us<a href='/seshmaster/'>Home</a>")

def site_map(request):
    return HttpResponse("Sitemap<a href='/seshmaster/'>Home</a>")

def contact(request):
    return HttpResponse("contact info<a href='/seshmaster/'>Home</a>")


