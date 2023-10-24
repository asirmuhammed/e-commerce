from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from .models import Subcategories,Categories,Product

# Create your views here.
class SubcategoriesList(ListView):
    model = Subcategories
    template_name = "product/subcategorie.html"

class CategoriesList(ListView):
    model = Categories
    template_name = "product/categories.html"

class ProductList(ListView):
    model = Product
    template_name = "product/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categorys"] = Categories.objects.all()
        return context
    

# class index (TemplateView,ListView):
#     model = Product
#     template_name = "product/index.html"



    