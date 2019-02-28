
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf.urls import include
from rango import views
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^seshmaster/', include('seshmaster.urls')),
	url(r'^$', views.index, name='index'),
]
