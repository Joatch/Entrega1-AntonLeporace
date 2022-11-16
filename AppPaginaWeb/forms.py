from django import forms

class CrearLibroForm(forms.Form):
    nombre = forms.CharField(max_length=40)
    autor = forms.CharField(max_length=40)

class CrearJuegoForm(forms.Form):
    nombre = forms.CharField(max_length=40)
    creador = forms.CharField(max_length=40)

class CrearSerieForm(forms.Form):
    nombre = forms.CharField(max_length=40)
    genero = forms.CharField(max_length=40)