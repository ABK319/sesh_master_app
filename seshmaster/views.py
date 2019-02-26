from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Howdy Sesh-head!<br/><a href='/seshmaster/about/'>About Us  |  </a><a href='/seshmaster/sitemap/'>Sitemap  |  </a><a href='/seshmaster/contact'>  Contact</a>")

def about(request):
    return HttpResponse("About Us<a href='/seshmaster/'>Home</a>")

def site_map(request):
    return HttpResponse("Sitemap<a href='/seshmaster/'>Home</a>")

def contact(request):
    return HttpResponse("contact info<a href='/seshmaster/'>Home</a>")


