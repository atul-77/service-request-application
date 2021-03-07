from django.urls import path
from api import views

urlpatterns = [
    path('api/', views.CustomerList),
    path('api/<int:pk>/', views.CustomerDetails),
    path('api/customers',views.GetCustomers.as_view())
]