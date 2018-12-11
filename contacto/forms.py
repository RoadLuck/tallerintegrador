from django import forms

class ContactoForm(forms.Form):
    nombre = forms.CharField(label="Nombre", required=True, widget=forms.TextInput(
        attrs={'class':'form-control','placeholder':'Nombre*'}
    ))
    email = forms.EmailField(label="Email", required=True, widget=forms.EmailInput(
        attrs={'class':'form-control','placeholder':'Email*'}
    ))
    asunto = forms.CharField(label="Asunto", required=True, widget=forms.TextInput(
        attrs={'class':'form-control','placeholder':'Asunto*'}
    ))
    mensaje = forms.CharField(label="Mensaje", required=True, widget=forms.Textarea(
        attrs={'class':'form-control','rows':9,'placeholder':'Mensaje*'}
    ))
