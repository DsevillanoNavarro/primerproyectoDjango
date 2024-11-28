from django.urls import path
from . import views

urlpatterns = [
    path('', views.principal, name='principal'),
    path('menu/', views.menu, name='menu'),
    path('<int:pk>', views.detalle_post, name='detalle_post'),
    path('autores/', views.autores, name='autores'),
    path('autores/<str:nautor>', views.detalle_autor, name='detalle_autor')
]
