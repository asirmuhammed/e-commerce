from django.db import models

# Create your models here.


class Categories(models.Model):
    category_name=models.CharField(max_length=10)
    category_image=models.ImageField()
    
    def __str__(self):
        return self.category_name
    
    

class Subcategories(models.Model):
    Category=models.ForeignKey(Categories, on_delete=models.CASCADE)
    subcategoty_name=models.CharField(max_length=10)
    

    def __str__(self):
        return self.subcategoty_name

class Product(models.Model):
    Subcategoty=models.ForeignKey(Subcategories, on_delete=models.CASCADE)
    product_name=models.CharField(max_length=50)
    product_img=models.ImageField(upload_to="product")
    product_price=models.CharField(max_length=10)

    def __str__(self):
        return self.product_name
