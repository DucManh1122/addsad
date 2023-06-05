from django.shortcuts import render
from . import cart

# Create your views here.
def show_cart(request):
    if request.method == 'POST': 
        postdata = request.POST.copy() 
        if postdata['submit'] == 'Remove': 
            cart.remove_from_cart(request) 
        if postdata['submit'] == 'Update': 
            cart.update_cart(request) 
    cart_items = cart.get_cart_items(request)
    page_title = 'Shopping Cart'
    cart_subtotal = cart.cart_subtotal(request)
    for item in cart_items:
        print(item.product.price)
    return render(request, 'cart/cart.html', {'cart_items':cart_items,
                                               'page_title':page_title,
                                                 'cart_subtotal':cart_subtotal})