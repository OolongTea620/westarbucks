from django.shortcuts import render
import json

from django.http import JsonResponse
from django.views import View

from products.models import Menu, Category, Product

class ProductsView(View):
    def post(self, request):
        data     = json.loads(request.body)
        menu     = Menu.objects.create(name=data['menu'])
        category = Category.objects.create(
            name = data['category'],
            menu = menu
        )
        Product.objects.create(
            name     = data['product'], 
            category = category,
            menu     = menu
        )
        return JsonResponse({'messasge':'created'}, status=201)
    
    def get(self, request):
        products = Product.objects.all()
        results  = []

        for product in products:
            results.append(
                {
                    "menu" : product.category.menu.name,
                    "category" : product.category.name,
                    "product_name" : product.name
                }
            )

        return JsonResponse({'resutls':results}, status=200)
