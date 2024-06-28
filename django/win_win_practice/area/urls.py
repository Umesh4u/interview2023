from django.urls import path
from .views import areas_list

urlpatterns = [
    path('list/',areas_list),
]
