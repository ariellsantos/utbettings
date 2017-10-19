from django.conf.urls import url
from . import views

app_name = "apuestas"

urlpatterns = [
    url(r'^$', views.index, name="index" ),
    url(r'^guardar_usuario/$', views.guardar_usuario ,  name="guardar_usuario"),
    url(r'^torneos_sin_rol/$', views.torneos_sin_rol, name="torneos_sin_rol"),
    url(r'^generar_rol/(?P<torneo>\d+)/$', views.generar_rol, name="generar_rol"),
    url(r'^juegos_torneo/(?P<torneo>\d+)/$', views.torneo, name="juegos"),
    url(r'^torneos_apuestas/$', views.torneos_apuestas, name="torneos_apuestas")
]