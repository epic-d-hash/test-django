from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def index(request):
    """
    Index Method
    """
    template = loader.get_template('secondPage.html')
    return HttpResponse(template.render())

def login_form(request):
    """
    Login Form
    """
    template = loader.get_template('first.html')
    return HttpResponse(template.render())