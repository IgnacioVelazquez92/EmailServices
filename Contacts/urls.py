from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registro, name='register'),
    path('', views.index, name="index"),
    path('logout/', views.cerrar_sesion, name='logout'),
    path('signin/', views.iniciar_sesion, name='signin')
]
