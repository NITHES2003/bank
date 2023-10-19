from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),
    path('dashboard/', views.dashboard, name = 'dashboard'),
    path('transactions/', views.transaction, name = 'transactions'),
    path('customers/', views.customers, name = 'customers'),
    

]
