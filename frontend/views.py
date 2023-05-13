from django.shortcuts import render
import requests

def home(request):
    response = requests.get("http://localhost:8000/api/products")
    data = response.json()
    return render(request, "index.html", {"products": data})


def product_details(request, id):
    response = requests.get(f"http://localhost:8000/api/product/{id}")
    data = response.json()
    return render(request, "product_page.html", {"product": data})