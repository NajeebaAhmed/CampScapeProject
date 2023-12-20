from django.db import models

class user(models.Model):
 FirstName = models.CharField(max_length=255, null=True)
 LastName = models.CharField(max_length=255, null=True)
 Phone = models.CharField(max_length=15, null=True)
 Email = models.CharField(max_length=255, null=True)
 password = models.CharField(max_length=255, null=True)
 def __str__(self) -> str:
    return self.FirstName + ' ' + self.LastName