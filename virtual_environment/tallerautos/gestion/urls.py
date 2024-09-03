from django.urls import path
from . import views  

urlpatterns = [
    path('', views.index, name='index'),
    path('ubicacion/', views.ubicacion, name='ubicacion'),
    path('agendar/', views.agendar, name='agendar'),
    path('servicios/', views.servicios, name='servicios'),
    path('login/', views.login, name='login'),
    path('agenda/', views.agenda, name='agenda'),
]