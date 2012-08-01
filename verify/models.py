from django.db import models
from django.contrib import admin

class Drug(models.Model):
	product_name = models.TextField(db_index=True,max_length=300)
	Generic_name = models.TextField(max_length=300,blank=True)
	strength = models.TextField(max_length=300,blank=True)
	dosage_form = models.TextField(max_length=300,blank=True)
	applicant= models.TextField(max_length=300,blank=True)
	manufacturer = models.TextField(max_length=300,blank=True)
	local_agent = models.TextField(max_length=300,blank=True)
	expiry_date = models.TextField(max_length=30,blank=True)
	
	
	def __unicode__(self):
		return(self.product_name)
	
	
	
class Food_water(models.Model):
	product_name = models.TextField(db_index=True,max_length=500)
	FDB_number = models.TextField(max_length=15,blank=True)
	manu_location = models.TextField(max_length=300,blank=True)
	dosage_form = models.CharField(max_length=30,blank=True)
	
	def __unicode__(self):
		return (self.product_name)
class Food_waterAdmin(admin.ModelAdmin):
    list_display=('product_name','FDB_number','manu_location')
    search_fields=('product_name','FDB_number','manu_location')
    list_filter=('FDB_number',)
	
class DrugAdmin(admin.ModelAdmin):
	list_display=('Generic_name','dosage_form','manufacturer','local_agent','expiry_date')
        search_fields=('product_name',)
admin.site.register(Food_water,Food_waterAdmin)
admin.site.register(Drug,DrugAdmin)

