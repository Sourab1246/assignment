from django.urls import path
from productsapi import views
from .views import Products,ProductsDetails

urlpatterns = [
    path('products/',views.ProductsList.as_view()), #give details of  all products,get and post method
    path('products/<int:id>/',views.ProductsDetails.as_view()),#give details by id,GET,PUT AND delete METHOD
    ]
