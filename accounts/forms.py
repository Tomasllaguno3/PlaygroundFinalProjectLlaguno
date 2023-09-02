from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User

class FormularioRegistro(UserCreationForm):

    email     = forms.EmailField(required=True)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:'' for k in fields}

class FormularioEditarPerfil(forms.Form):

    email       = forms.EmailField(required=True, widget=forms.EmailInput(attrs={ 'class' : 'form-control' }))
    first_name  = forms.CharField(required=False, widget=forms.TextInput(attrs={ 'class' : 'form-control' }), label='Nombre')
    last_name   = forms.CharField(required=False, widget=forms.TextInput(attrs={ 'class' : 'form-control' }), label='Apellido')
    avatar      = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={ 'class' : 'form-control' }))
    descripcion = forms.CharField(max_length=255, required=False, widget=forms.Textarea(attrs={ 'class' : 'form-control' }))
    link        = forms.URLField(max_length=100, required=False, widget=forms.TextInput(attrs={ 'class' : 'form-control' }))


class FormularioCambiarPassword(PasswordChangeForm):

    old_password  = forms.CharField(widget=forms.PasswordInput(attrs={ 'class' : 'form-control' }), label='Password actual')
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={ 'class' : 'form-control' }), label='Password nuevo')
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={ 'class' : 'form-control' }), label='Confirmar password')

    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']
        help_texts = {k:'' for k in fields}