from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('nouveau/', views.add_visit, name='add_visit'),
    path('visiteurs/', views.liste_visiteurs, name='liste_visiteurs'),
    path('historique/', views.historique, name='historique'),
    path('checkout/<int:pk>/', views.checkout_visit, name='checkout_visit'),
    path('delete/<int:pk>/', views.delete_visit, name='delete_visit'),
    path('visiteurs/', views.liste_visiteurs, name='liste_visiteurs'),
    path('start-visit/<int:pk>/', views.start_visit, name='start_visit'),
]