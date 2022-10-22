from django.urls import path

from . import views

urlpatterns = [
    path('deposit/', views.deposit),
    path('withdraw/', views.withdraw),
    path('transfer/', views.transfer),
]