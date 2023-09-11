from django.db import models
from django.conf import settings

from django.utils.translation import gettext as _

class Order(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_('User'))
    is_paid = models.BooleanField(verbose_name=_('Is Paid?'), default=False)
    
    first_name = models.CharField(verbose_name=_('First Name'), max_length=120)
    last_name = models.CharField(verbose_name=_('Last Name'), max_length=120)
    phone_number = models.CharField(verbose_name=_('Phone Number'), max_length=15)
    address = models.CharField(verbose_name=_('Address'), max_length=700)
    order_notes = models.CharField(verbose_name=_('Order Notes'), max_length=700)

    datetime_created = models.DateTimeField(verbose_name=_('Created at'), auto_now_add=True)
    datetime_modified = models.DateTimeField(verbose_name=_('Modified at'), auto_now=True)


    def __str__(self):
        return f'Order: {self.id}'


class OrderItem(models.Model):
    order = models.ForeignKey(to=Order, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(to='products.Product', related_name="order_items", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.PositiveIntegerField()


    def __str__(self):
        return f'OrderItem {self.id}: Product {self.product} x {self.quantity} - {self.price}'
