from django.db import models
from django.contrib import admin

class Product(models.Model):
	product_name = models.CharField(max_length=60)
	FDB_number = models.CharField(max_length=15)
	manu_location = models.CharField(max_length=100)
	strength = models.CharField(max_length=30)
	dosage_form = models.CharField(max_length=30)
	local_agent = models.CharField(max_length=100)
	expiry_date = models.DateField()
	
	
	def __unicode__(self):
		return self.product_name

admin.site.register(Product)

