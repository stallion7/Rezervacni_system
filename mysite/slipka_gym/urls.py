from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('rezervace/', views.rezervace, name='rezervace'),
    path('rezervace/<int:year>/<str:month>/', views.rezervace, name='rezervace'),
    path('uvod_prihlaseny/', views.uvod, name='uvod_prihlaseny'),
    path('trenink/', views.add_trenink, name='add-trenink'),
    path('seznam_treninku/', views.seznam_treninku, name='seznam-treninku'),
    path('show_trenink/<trenink_id>', views.show_trenink, name='show-trenink'),
    path('update_trenink/<trenink_id>', views.update_trenink, name='update-trenink'),
    path('delete_trenink/<trenink_id>', views.delete_trenink, name='delete-trenink'),

]