from django.db import models
from django.contrib import admin

class Drug(models.Model):
	product_name = models.TextField(max_length=300)
	Generic_name = models.TextField(max_length=300,blank=True)
	strength = models.CharField(max_length=30,blank=True)
	dosage_form = models.CharField(max_length=30,blank=True)
	applicant= models.CharField(max_length=100,blank=True)
	manufacturer = models.TextField(max_length=300,blank=True)
	local_agent = models.TextField(max_length=300,blank=True)
	expiry_date = models.CharField(max_length=10,blank=True)
	
	
	def __unicode__(self):
		return(self.product_name)
	
	
	
class Food_water(models.Model):
	product_name = models.TextField(max_length=500)
	FDB_number = models.TextField(max_length=15,blank=True)
	manu_location = models.TextField(max_length=300,blank=True)
	dosage_form = models.CharField(max_length=30,blank=True)
	
	def __unicode__(self):
		return (self.product_name)
class ProductAdmin(admin.ModelAdmin):
    list_display=('product_name','FDB_number','manu_location','strength')
    list_filter=('product_name','FDB_number')

admin.site.register(Food_water)
admin.site.register(Drug)

