from django.conf.urls import url
from seshmaster import views

urlpatterns = [
url(r'^$', views.index, name='index'),
url(r'about/', views.about, name='about'),
url(r'contact/', views.contact, name='contact'),
url(r'signup/', views.signup, name='signup'),
url(r'^login/$', views.user_login, name='login'), 
url(r'nightclubbrowse/', views.nightclubbrowse, name='nightclubbrowse'),
<<<<<<< HEAD
url(r'nightclubpage/', views.nightclubpage, name='nightclubpage'),	
url(r'leavereview/', views.leavereview, name='leavereview'),	
url(r'rateimage/', views.rateimage, name='rateimage'),
url(r'addlocation/', views.addlocation, name='addlocation'),
url(r'^logout/$', views.user_logout, name='logout'),
url(r'addNCimage', views.addNCimage, name='addNCimage'),
=======
url(r'nightclubbrowse/nightclubpage/', views.nightclubpage, name='nightclubpage'),	
url(r'nightclubbrowse/leavereview/', views.leavereview, name='leavereview'),	
url(r'nightclubbrowse/rateimage/', views.rateimage, name='rateimage'),
url(r'addlocation/', views.addlocation, name='addlocation'),
url(r'^logout/$', views.user_logout, name='logout'),
>>>>>>> e655d28cad41fab5061c8343832b51efc5071976

#url(r'/', views., name=''),						#template line
]

