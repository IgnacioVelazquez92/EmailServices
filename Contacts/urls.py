from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.registro, name='register'),
    path('', views.index, name="index"),
    path('logout/', views.cerrar_sesion, name='logout'),
    path('signin/', views.iniciar_sesion, name='signin'),

    # CRUD para ContactList
    path('dashboard/', views.contact_list_dashboard,
         name='contact_list_dashboard'),
    path('create/', views.create_contact_list, name='create_contact_list'),
    path('edit/<int:pk>/', views.edit_contact_list, name='edit_contact_list'),
    path('delete/<int:pk>/', views.delete_contact_list,
         name='delete_contact_list'),
    path('add-email/<int:contact_list_id>/',
         views.add_contact_email, name='add_contact_email'),
    path('delete-email/<int:email_id>/',
         views.delete_contact_email, name='delete_contact_email'),
    path('list/<int:pk>/', views.list_detail, name='list_detail'),
    path("edit_user/", views.edit_user, name="edit_user"),
]
