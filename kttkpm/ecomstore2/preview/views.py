from django.shortcuts import render

# Create your views here.
def home(request):
    context = {'site_name': 'Modern Musician'}
    return render(request,'index.html',context)