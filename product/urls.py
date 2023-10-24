from django.urls import path
from . import views
from django.views.generic import ListView


app_name = "product"

urlpatterns = [
    path("",views.ProductList.as_view(),name="product"),
    path("categories",views.CategoriesList.as_view(),name="Categories"),
    path("subcategories",views.SubcategoriesList.as_view(),name="subcategories"),
    
    
]