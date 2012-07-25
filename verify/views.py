from django.shortcuts import redirect
from django.template import Context, loader
from django.http import HttpResponse
from django.shortcuts import render_to_response
from models import Product 
from django.forms import ModelForm
from django import forms
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from verify.models import Product
from django.core.exceptions import ObjectDoesNotExist


class searchForm(forms.Form):
    search_product = forms.CharField()
   

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
			try:		
				posts =Product.objects.get(product_name__iexact= search_product)
				argument = 'verify/search.html/'
				exist='True'
				t = loader.get_template(argument)
				c = Context({'posts':posts,'term':term, 'search_product':search_product,'exist':exist})
				return HttpResponse(t.render(c))
			except Product.DoesNotExist:
	  			argument = 'verify/search.html/'
				t = loader.get_template(argument)
				exist='False'
				c = Context({'term':term, 'search_product':search_product,'exist':exist})
				return HttpResponse(t.render(c))
	  			

		
			
		
		
        
        
        


        

        
  

