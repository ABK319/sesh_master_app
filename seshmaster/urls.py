from django.conf.urls import url
from seshmaster import views

urlpatterns = [
url(r'^$', views.index, name='index'),
url(r'about/', views.about, name='about'),
url(r'contact/', views.contact, name='contact'),
url(r'signup/', views.signup, name='signup'),
url(r'^login/$', views.user_login, name='login'), 
url(r'images/', views.search_img, name='images'),
url(r'addlocation/', views.addlocation, name='addlocation'),
url(r'^logout/$', views.user_logout, name='logout'),
url(r'^search/$', views.search, name='search'),
url(r'addlocation/', views.addlocation, name='addlocation'),
url(r'^logout/$', views.user_logout, name='logout'),
#url(r'/', views., name=''),						#template line
]

