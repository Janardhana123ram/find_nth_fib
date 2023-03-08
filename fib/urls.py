from django.urls import path

from . import views

urlpatterns = [
     path('fibonaccis', views.fibonacci_list),
     path('fibonacci', views.fibonacci_detail)
]
