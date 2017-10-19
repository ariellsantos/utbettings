from django.conf.urls import url, include
from django.contrib import admin
from basicos import views
from apuestas import views as vap


urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^admin/', admin.site.urls),
    url(r'^apuestas/', include('apuestas.urls')), 
    url(r'^login/$', vap.login_user, name="login"),
    url(r'^logout/$', vap.logout_user, name="logout"),
]