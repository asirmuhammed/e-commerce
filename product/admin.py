from django.contrib import admin
from .models import Categories
from .models import Subcategories
from .models import Product

# Register your models here.
@admin.register(Product)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ("product_name", "product_price")

@admin.register(Categories)
class RegistrationAdmin(admin.ModelAdmin):
    pass

@admin.register(Subcategories)
class RegistrationAdmin(admin.ModelAdmin):
    pass