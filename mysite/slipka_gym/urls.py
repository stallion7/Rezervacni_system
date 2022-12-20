from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('rezervace/', views.rezervace, name='rezervace'),
    path('rezervace/<int:year>/<str:month>/', views.rezervace, name='rezervace'),
    path('uvod_prihlaseny/', views.uvod, name='uvod_prihlaseny'),
    path('trenink/', views.add_trenink, name='add-trenink'),
    path('rezervace/', views.trenink, name='trenink')
]