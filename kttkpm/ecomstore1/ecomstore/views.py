from django.http import HttpResponse
from django.shortcuts import render


def catalog(request): 
    my_context = { 'site_name': 'Modern Musician' } 
    return render(request, 'sample.html', my_context) 