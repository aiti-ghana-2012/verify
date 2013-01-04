from django.shortcuts import redirect
from django.template import Context, loader
from django.http import HttpResponse
from django.shortcuts import render_to_response
from models import Drug ,Food_water 
from django.forms import ModelForm
from django import forms
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from verify.models import Drug ,Food_water
from django.core.exceptions import ObjectDoesNotExist

import dj_simple_sms

def home(request):
	
        return render_to_response('verify/base.html',{})
        
@csrf_exempt        
def search(request,term):
        search_product=request.POST.get('search_product')
        if (search_product==''):
        	if (request.path=="/verify/search/"):
			request.path='verify/base.html/'
			print request.path
			return render_to_response(request.path,{})
		"""else:
		    print request.path
		    request.path='/verify/search/'
		    print "fjhjhgjhgv"
		    print request.path*2
		    return render_to_response(request.path,{})"""




	
        else:
			
			"""try:		
				posts =Food_water.objects.filter(product_name__iexact= search_product)
				print bool(posts)
				argument = 'verify/search.html/'
				exist='True'
				t = loader.get_template(argument)
				c = Context({'posts':posts, 'search_product':search_product,'exist':exist})
				return HttpResponse(t.render(c))
			except ObjectDoesNotExist:
	  			print 'jhkjhkjbkjb'
	  			try:		
					posts =Drug.objects.filter(product_name__iexact= search_product)
					argument = 'verify/search.html/'
					exist='True'
					t = loader.get_template(argument)
					c = Context({'posts':posts, 'search_product':search_product,'exist':exist})
					return HttpResponse(t.render(c))
				except ObjectDoesNotExist:
		  			argument = 'verify/search.html/'
					t = loader.get_template(argument)
					exist='False'
					c = Context({ 'search_product':search_product,'exist':exist})
					return HttpResponse(t.render(c))"""
			if ('fdb' in search_product.lower()):
				print "fdb entered"
				if(bool(Food_water.objects.filter(FDB_number__iexact= search_product))):
					posts =Food_water.objects.filter(FDB_number__iexact= search_product)
					print bool(posts)
					argument = 'verify/search.html/'
					exist='True'
					t = loader.get_template(argument)
					c = Context({'posts':posts, 'search_product':search_product,'exist':exist})
					return HttpResponse(t.render(c))
				else:
					argument = 'verify/search.html/'
					t = loader.get_template(argument)
					exist='False'
					c = Context({ 'search_product':search_product,'exist':exist})
					return HttpResponse(t.render(c))

	  			

			if(bool(Food_water.objects.filter(product_name__iexact= search_product))):
				posts =Food_water.objects.filter(product_name__iexact= search_product)
				print bool(posts)
				argument = 'verify/search.html/'
				exist='True'
				t = loader.get_template(argument)
				c = Context({'posts':posts, 'search_product':search_product,'exist':exist})
				return HttpResponse(t.render(c))
			else:
				if(bool(Drug.objects.filter(product_name__iexact= search_product))):
					posts =Drug.objects.filter(product_name__iexact= search_product)
					argument = 'verify/search.html/'
					exist='True'
					t = loader.get_template(argument)
					c = Context({'posts':posts, 'search_product':search_product,'exist':exist})
					return HttpResponse(t.render(c))
				else:
					argument = 'verify/search.html/'
					t = loader.get_template(argument)
					exist='False'
					c = Context({ 'search_product':search_product,'exist':exist})
					return HttpResponse(t.render(c))
"""					
@csrf_exempt        
def searchtryout(request,term):
        message=[]
        search_product=request.POST.get('search_product')
         	
			if(bool(Food_water.objects.filter(product_name__iexact= search_product))):
				posts =Food_water.objects.filter(product_name__iexact= search_product)
				for post in posts:
					message.append('Product Details: '+post.product_name+', '+ post.FDB_number+', '+post.manu_location)
				return message
				
			
			elif(bool(Drug.objects.filter(product_name__iexact= search_product))):
				posts =Drug.objects.filter(product_name__iexact= search_product)
				for post in posts:
					message.append('Product Details: '+post.product_name+', '+ post.strength+', '+post.dosage_form)
				print message
				return message
							
				
			else:
				message = 'Product not Verified '
				print message
				return message					
					
					
def sms(request,term):
	message=''
        search_product= sms.body
        if (search_product==''):
        	message="Please you sent blank Message"
        	return message
		
        else:
			if(bool(Food_water.objects.filter(product_name__iexact= search_product))):
				posts =Food_water.objects.filter(product_name__iexact= search_product)
				for post in posts:
					message.append('Product Details: '+post.product_name+', '+ post.FDB_number+', '+post.manu_location)
				return message
				
			
			elif(bool(Drug.objects.filter(product_name__iexact= search_product))):
				posts =Drug.objects.filter(product_name__iexact= search_product)
				for post in posts:
					message.append('Product Details: '+post.product_name+', '+ post.strength+', '+post.dosage_form)
				print message
				return message
							
				
			else:
				message = 'Product not Verified '
				print message
				return message		"""


        
def sms_search(sms):
        message=''
        search_product= sms.body.strip()
        if (search_product==''):
        	message="You sent blank message\n Please check and try again.\nVeryFi\nBuy with confidence."

		
        else:		
			if ('fdb' in search_product.lower()):
				if(bool(Food_water.objects.filter(FDB_number__iexact= search_product))):
					posts =Food_water.objects.filter(FDB_number__iexact= search_product)
					for post in posts:
						message+='Product Details \n Name : '+post.product_name+'\n FDB number :'+ post.FDB_number+' \n Manufacturer : '+post.manu_location
						message+='\n'
				else:
					message = search_product+'  MAY BE FAKE call FDB on \n 0302233200 or 0302229261'
					
			elif(bool(Food_water.objects.filter(product_name__iexact= search_product))):
				posts =Food_water.objects.filter(product_name__iexact= search_product)	
				for post in posts:
					message+='Product Details \n Name : '+post.product_name+'\n FDB number :'+ post.FDB_number+' \n Manufacturer : '+post.manu_location
					message+='\n'
			elif(bool(Drug.objects.filter(product_name__iexact= search_product))):
				posts =Drug.objects.filter(product_name__iexact= search_product)
				for post in posts:
					message+= 'Product Details \n Name: '+post.product_name+'\n Strength: '+ post.strength+'\n Dosage: '+post.dosage_form +'\n Local Agent: '+post.local_agent #+'\n Expire Date: '+post.expiry_date
					message+='\n'
			else:
				message = search_product+'  MAY BE FAKE call FDB on \n 0302233200 or 0302229261'
				
        
        response = dj_simple_sms.models.SMS(to_number=sms.from_number, from_number='verify', body=message)
        response.send()
  #  response.send()	
  #  print "The search term is: %s" % sms.body
#
 #   response = SMS(to_number=sms.from_number, from_number='verify', body="no foods found")
  #  response.send()

        
  

