from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from cart.cart import add_to_cart
from . import models
from .forms import ProductAddToCartForm

# Create your views here.
def show_category(request, category_slug):
    c = get_object_or_404(models.Category, slug=category_slug)
    products = models.Product.objects.filter(categories=c)
    # page_title = c.name 
    # meta_keywords = c.meta_keywords 
    # meta_description = c.meta_description
    return render(request, 'catalog/category.html', {'products': products})

# new product view, with POST vs GET detection
def show_product(request, product_slug):
    p = get_object_or_404(models.Product, slug=product_slug)
    categories = p.categories.filter(is_active=True)
    # need to evaluate the HTTP method 
    if request.method == 'POST': 
        # add to cart…create the bound form 
        postdata = request.POST.copy() 
        form = ProductAddToCartForm(request, postdata) 
        #check if posted data is valid 
        if form.is_valid(): 
            #add to cart and redirect to cart page
            add_to_cart(request) 
            # if test cookie worked, get rid of it 
            if request.session.test_cookie_worked(): 
                request.session.delete_test_cookie() 
            url = reverse('show_cart') 
            return HttpResponseRedirect(url)
    else:
        # it’s a GET, create the unbound form. Note request as a kwarg 
        form = ProductAddToCartForm(request=request, label_suffix=':')
    # assign the hidden input the product slug 
    form.fields['product_slug'].widget.attrs['value'] = product_slug 
    # set the test cookie on our first GET request 
    request.session.set_test_cookie() 
    return render(request, 'catalog/product.html', {'categories': categories, 'p':p, 'form':form})

def home(request):
    return render(request, 'catalog/index.html')