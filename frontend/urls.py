from django.urls import path
from frontend import views

urlpatterns = [
    path('',views.home), #give details of  all products,get and post method
    path('products/<int:id>/',views.product_details),#give details by id,GET,PUT AND delete METHOD
    ]