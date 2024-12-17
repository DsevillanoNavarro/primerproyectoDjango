from datetime import date
from django import forms
from django.forms import ModelForm, Textarea, ValidationError
from blog.models import Post, Autor
class post_form(forms.Form):
    titulo = forms.CharField(label="Título",max_length=200)
    autor = forms.IntegerField(label="AutorID")
    cuerpo = forms.CharField(label="Cuerpo", widget=forms.Textarea)
    fpublicado = forms.DateField(label="Fecha de publicación")

    
    
class post_form_model(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["titulo", "autor", "cuerpo","fecha"]
        
    def clean_fecha(self):
        fecha = self.cleaned_data['fecha']
        if fecha > date.today():
            raise ValidationError("La fecha de publación no puede ser mayor a la actual")
        return fecha

class form_autores_model(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ["nombre", "apellidos", "email","dni","bio"]