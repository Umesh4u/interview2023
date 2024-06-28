from django.urls import path
from .views import StudentData

urlpatterns = [
    path('api/',StudentData.as_view()),
]
