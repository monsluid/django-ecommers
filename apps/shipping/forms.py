from django import forms
from apps.shipping.models import Shipping


# -------------------------------------------------------->
# Forms Shipping

class ShippingForm(forms.ModelForm):
    class Meta:
        model = Shipping
        fields = (
            'quantity',
            'product',
            
        )
        labels = {
            'product': 'Producto',
            'quantity': 'Cantidad', 
        }
        widgets = {
            'quantity': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cantidad' }),
        }