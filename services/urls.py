from django.urls import path
from .views import ServicesList, CreateService, UpdateServis, DeleteServis
urlpatterns = [
    path('', ServicesList.as_view(), name='servis_list'),
    path('create/', CreateService.as_view(), name='servis_add'),
    path('update/<int:pk>/', UpdateServis.as_view(), name='servis_update'),
    path('delete/<int:pk>/', DeleteServis.as_view(), name='servis_delete'),
]