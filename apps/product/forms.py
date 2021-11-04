from django import forms
from apps.product.models import Category, Brand, State, Product


# -------------------------------------------------------->
# Forms Brand

class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = (
            'name',
            'description',
        )
        labels = {
            'name': 'Nombre',
            'description': 'Descripcion',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
        }


# -------------------------------------------------------->
# Forms Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = (
            'name',
            'description',
        )
        labels = {
            'name': 'Nombre',
            'description': 'Descripcion',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
        }


# -------------------------------------------------------->
# Forms State

class StateForm(forms.ModelForm):
    class Meta:
        model = State
        fields = (
            'name',
            'description',
        )
        labels = {
            'name': 'Nombre',
            'description': 'Descripcion',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
        }


# -------------------------------------------------------->
# Product Forms

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = (
            'idProduct',
            'name',
            'category',
            'brand',
            'state',
            'price',
            'description',
            'picture',
            'stock',
        )
        labels = {
            'idProduct': 'ID',
            'name': 'Nombre',
            'category': 'Categoria',
            'brand': 'Marca',
            'state': 'Estado',
            'price': 'Costo',
            'description': 'Descripcion',
            'picture': 'Imagen',
            'stock': 'Piezas en Almacen',
        }
        widgets = {
            'idProduct': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'brand': forms.Select(attrs={'class': 'form-control'}),
            'state': forms.Select(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'picture': forms.ClearableFileInput(attrs={'class':'form-control-file'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
        }



