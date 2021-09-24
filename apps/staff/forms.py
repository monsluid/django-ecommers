from django import forms
from apps.staff.models import Staff, Role
from django.contrib.auth.models import User


# -------------------------------------------------------->
# Forms User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'last_name',
            'first_name',
            'email',
        )
        labels = {
            'username': 'Nombre de usuario',
            'last_name': 'Nombre',
            'first_name': 'Apellido',
            'password': 'Password',
            'email': 'Correo electronico'
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control' }),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }


# -------------------------------------------------------->
# Forms role

class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = (
            'name',
            'description',
        )
        labels = {
            'name': 'Nombre Del Rol',
            'description': 'Descripcion del rol',
        }


# -------------------------------------------------------->
# Form staff

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = [
            'idStaff',
            'name',
            'phone',
            'email',
            'user',
            'role',

        ]

        labels = {
            'idStaff': 'Id',
            'name': 'Name',
            'phone': 'Telefono',
            'email': 'Correo Electronico',
            'user': 'Usuario',
            'role': 'Rol',

        }

        widgets = {
            'idStaff': forms.TextInput(
                attrs={
                    'class': 'form-control',

                }
            ),
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'phone': forms.TextInput(
                attrs={
                    'class': 'form-control',

                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'user': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'role': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),


        }
