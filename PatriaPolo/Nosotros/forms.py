# Create your forms here

from unittest.util import _MAX_LENGTH
from django import forms

class NosotrosForm(forms.Form):
    nombre=forms.CharField(label='Nombre', max_length=20, required=True)
    apellido=forms.CharField(label='Apellido', max_length=20, required=True)
    email=forms.EmailField(label='Email', max_length=50, required=True)
    telefono=forms.CharField(label='Telefono', max_length=15, required=False)
    mensaje=forms.CharField(label='Mensaje (150 caracteres)', max_length=150, widget=forms.Textarea, required=True)



