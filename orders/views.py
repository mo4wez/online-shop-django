from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from cart.cart import Cart
from .forms import OrderForm
from .models import OrderItem

@login_required
def order_create_view(request):
    cart = Cart(request)
    order_form = OrderForm()

    if request.method == 'POST':
        order_form = OrderForm(request.POST,)

        if order_form.is_valid():
            order_obj = order_form.save(commit=False)
            order_obj.user = request.user
            order_obj.save()

            for item in cart:
                product = item['product_obj']
                OrderItem.objects.create(
                    order = order_obj,
                    product = product,
                    quantity = item['quantity'],
                    price = product.price,
                )
            
            cart.clear()


    return render(request, 'orders/order_create.html', context={'form': order_form,})
