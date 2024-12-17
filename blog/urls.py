from django.urls import path
from . import views

urlpatterns = [
    path('', views.principal, name='principal'),
    path('menu/', views.menu, name='menu'),
    path('<int:pk>', views.detalle_post, name='detalle_post'),
    path('ji/', views.ji, name ='ji'),
    path('post_new/', views.post_new, name ='post_new'),
    path('post_edit/<int:pk>', views.post_edit, name ='post_edit'),
    path('autores/', views.autores, name='autores'),
    path('autores/new', views.autores_new, name='autores_new'),
    path('autores/<int:pk>', views.detalle_autores, name='detalle_autores'),
    path('autores/<int:pk>/edit', views.edit_autores, name='edit_autores'),
    path('autores/<int:pk>/delete', views.delete_autores, name='delete_autores'),
]
