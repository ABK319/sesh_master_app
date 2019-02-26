from django.conf.urls import url
from seshmaster import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about', views.about, name='about'),
    url(r'^sitemap', views.site_map, name='site_map'),
    url(r'^contact', views.contact, name='contact'),
]
