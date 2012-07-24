from django.db import models
from django.contrib import admin

class Product(models.Model):
    name = models.CharField(max_length=60)
    category = models.TextField()
    description = models.TextField()
    
    
    def __unicode__(self):
       return self.name

admin.site.register(Product)

