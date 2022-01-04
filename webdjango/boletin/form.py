from django import forms

class RegForm(forms.Form):
    nombre = forms.CharField()
    email = forms.EmailField()
    edad = forms.IntegerField()
    sexo = forms.ChoiceField(choices=(('M','Mujer'),('H','Hombre')))
    pais = forms.ChoiceField(choices=(('CO','Colombia'),('ES','España'),('MX','Mexico')))
    terminos = forms.BooleanField(required=True)