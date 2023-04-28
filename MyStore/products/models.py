from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class ProductCategory(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.name


# class User(AbstractUser):
#     pass
#






class Product(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(null=True,blank=True)
    price = models.DecimalField(max_digits=6,decimal_places=2 , default=0)
    quontity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE , default = 1)
    is_active = models.BooleanField(default=True)
    rating_value = models.DecimalField(max_digits=6, decimal_places=2,default=0.0)
    rating_count = models.IntegerField(default=0)
    def __str__(self):
        return self.name



class Like(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class comments(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    comment = models.TextField(null = False , default = "" , blank = True)
    commment_date = models.DateTimeField(null = True)
    product = models.ForeignKey(Product,on_delete = models.CASCADE)

def product_image_upload_path(instance, filename):
    return f'product_images/{instance.product.name}/{filename}'

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to=product_image_upload_path)

    def __str__(self):
        return self.image.name













