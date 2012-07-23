from django.shortcuts import redirect
from django.template import Context, loader
from django.http import HttpResponse
from django.shortcuts import render_to_response
from models import Product 
from django.forms import ModelForm
from django import forms
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect


def home(request):
        print 'it works'
        return HttpResponse('trialssss 1?') 
	##return render_to_response('verify/base.html',{})
