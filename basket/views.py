from django.shortcuts import render, redirect

# Create your views here.

def basket(request):
    """A View to return the users basket"""
    return render(request, 'basket/basket.html')

def add_to_basket(request, item_id):
    """ Add the requested item to the basket"""

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})


    if item_id in list(basket.keys()):
        basket[item_id] += quantity
    else:
        basket[item_id] = quantity

    request.session['basket'] = basket
    return redirect(redirect_url)
