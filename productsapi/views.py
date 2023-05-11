from django.shortcuts import render
from .models import Products
from .serializers import ProductsSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.http import HttpResponse,JsonResponse

# Create your views here.
class ProductsList(APIView):
    def get(self,request):

      products=Products.objects.all()
      serializer=ProductsSerializer(products,many=True)
      return JsonResponse(serializer.data,safe=False)
    
    def post (Self,request):
       serializer=ProductsSerializer(data=request.data)
       if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=status.HTTP_201_CREATED)
       return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class ProductsDetails(APIView):    
    
    def get_object(self, id):
        try:
            return Products.objects.get(id=id)
        except Products.DoesNotExist:
             return JsonResponse(status=status.HTTP_404_NOT_FOUND)
        
    def get(self,request,id):
        products=self.get_object(id)
        serializer=ProductsSerializer(products)
        return JsonResponse(serializer.data)
    
    def put(self,request,id):
        products=self.get_object(id)
        serializer=ProductsSerializer(products,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id):
            products=self.get_object(id)
            
            products.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    def patch(self,request,id):
        products=self.get_object(id)
        serializer=ProductsSerializer(products,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
        

# class ProductsAPIView(APIView):
#     def patch(self,request,id):
#         try:
#             products=Products.objects.get(id=id)
#         except products.DoesNotExist:
#             return JsonResponse(status=status.HTTP_404_NOT_FOUND)

#         serializer=ProductsSerializer(products,data=request.data,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)




            





       
       
