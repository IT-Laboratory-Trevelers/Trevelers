from django.shortcuts import render
from django.template import Context, loader
from django.template.loader import get_template
from django.http import HttpResponse

def homepage(request):
	template = get_template('firstpage.html')
	return HttpResponse(template.render())