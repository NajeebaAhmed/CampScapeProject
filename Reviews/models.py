from Packages.models import Package
from django.db import models



# Create your models here.


class Review(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE, null=True)
    username = models.CharField(max_length=60)
    body = models.TextField()

    def __str__(self):
        return self.username + '|' + str(self.package) 