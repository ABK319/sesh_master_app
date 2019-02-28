from django.conf.urls import url
from rango import views

urlpatterns = [
url(r'^$', views.index, name='index'),
url(r'contactus/', views.contactus, name='contactus'),
url(r'signup/', views.signup, name='signup'),
url(r'login/', views.login, name='login'),
url(r'nightclubbrowse/', views.nightclubbrowse, name='nightclubbrowse'),
url(r'nightclubbrowse/nightclubpage/', views.nightclubpage, name='nightclubpage'),	
url(r'nightclubbrowse/leavereview/', views.leavereview, name='leavereview'),	
url(r'nightclubbrowse/rateimage/', views.rateimage, name='rateimage'),			
#url(r'/', views., name=''),						#template line
]

