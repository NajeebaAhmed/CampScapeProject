from django.db import models
from django.contrib.auth.models import User


class Package(models.Model):
    name = models.CharField(max_length=255) 
    author = models.CharField(max_length=100, default='Unknown')
    min_members = models.PositiveIntegerField()
    max_members = models.PositiveIntegerField()
    description = models.TextField()
    product_description = models.TextField(null=True)
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to='package_images/',null=True)
    image2 = models.ImageField(upload_to='package_images/',null=True)
    image3 = models.ImageField(upload_to='package_images/',null=True)
    image4 = models.ImageField(upload_to='package_images/',null=True)
    
    def __str__(self):
        return self.name  
    
class PackageDetails(models.Model):
 package = models.ForeignKey(Package, on_delete=models.CASCADE, null=True)
 date = models.DateField(max_length=255, null=True) 
 time = models.TimeField(max_length=255, null=True) 
 special_request = models.CharField(max_length=255, null=True)

