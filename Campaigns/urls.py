from django.urls import path
from . import views

urlpatterns = [
    path('', views.campaign_list, name='campaign_list'),
    path('create/', views.create_campaign, name='create_campaign'),
    path('<int:campaign_id>/', views.campaign_detail, name='campaign_detail'),
    path('campaign/<int:pk>/edit/', views.edit_campaign, name='campaign_edit'),
    path('<int:campaign_id>/delete/',
         views.delete_campaign, name='campaign_delete'),
    path('<int:campaign_id>/send/', views.send_campaign, name='send_campaign'),
]
