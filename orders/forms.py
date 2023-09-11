from django import forms
from django.forms import ModelForm
from django.utils.translation import gettext as _

from .models import Order

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'phone_number', 'address', 'order_notes']
        widgets = {
            'address': forms.Textarea(attrs={
                'rows': 3,
            }),
            'order_notes': forms.Textarea(attrs={
                'rows': 5,
                'placeholder': _('Enter your order note (Optional).'),
            })
        }