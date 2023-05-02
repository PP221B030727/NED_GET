from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(null=True,blank=True)
    price = models.DecimalField(max_digits=6,decimal_places=2 , default=0)
    quontity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE , default = 1)
    is_active = models.BooleanField(default=True)
    rating_value = models.DecimalField(max_digits=6, decimal_places=2,default=0.0)
    rating_count = models.IntegerField(default=0)
    comments = models.ManyToManyField(User, through='Comment')

    def __str__(self):
        return self.name





class Comment(models.Model):
    product = models.ForeignKey(Product , on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(null=False, default="", blank=True)
    commment_date = models.DateTimeField(null=True)






def product_image_upload_path(instance, filename):
    return f'product_images/{instance.product.name}/{filename}'

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to=product_image_upload_path)

    def __str__(self):
        return self.image.name













