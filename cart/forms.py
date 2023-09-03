from django import forms

class AddToCartProductForm(forms.Form):
    QUANTUTY_CHOICES = [(i, str(i)) for i in range(1,11)]

    quantity = forms.TypedChoiceField(choices=QUANTUTY_CHOICES, coerce=int)

    inplace = forms.BooleanField(required=False, widget=forms.HiddenInput)
