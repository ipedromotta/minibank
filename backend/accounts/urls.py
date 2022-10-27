from django.urls import path

from . import views

urlpatterns = [
    path('deposit/', views.deposit),
    path('withdraw/', views.withdraw),
    path('transfer/', views.transfer),
    path('transactions/', views.get_transactions),
    path('update/', views.alter_user),
]