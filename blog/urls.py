from django.urls import path
from . import views

urlpatterns = [
    path('', views.principal, name='principal'),
    path('menu/', views.menu, name='menu')
]
