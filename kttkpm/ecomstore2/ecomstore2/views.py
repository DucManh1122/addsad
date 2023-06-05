from django.shortcuts import render
def file_not_found_404(request,exception): 
    return render(request,'404.html')  
