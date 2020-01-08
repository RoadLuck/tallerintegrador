from django import forms

SERVICIOS_DISPONIBLES=(('', '----'),('SISTEMA TIPO S','Sistema Tipo S'),('SISTEMA TIPO V','Sistema Tipo V'),('MALLA PROTECCION DE FACHADAS','Malla protección de fachadas'))

class CotizacionForm(forms.Form):
    nombre_c = forms.CharField(label="Nombre", required=True, widget=forms.TextInput(
        attrs={'class':'form-control','placeholder':'Nombre*'}
    ))
    apellido = forms.CharField(label="Apellido", required=True, widget=forms.TextInput(
        attrs={'class':'form-control','placeholder':'Apellido*'}
    ))
    rut = forms.IntegerField(label="Rut", required=True, widget=forms.TextInput(
        attrs={'class':'form-control','placeholder':'rut*'}
    ))
    telefono = forms.IntegerField(label="Celular", required=False, widget=forms.TextInput(
            attrs={'class':'form-control','placeholder':'Celular'}
        ))
    empresa = forms.CharField(label="Empresa", required=True, widget=forms.TextInput(
        attrs={'class':'form-control','rows':9,'placeholder':'Empresa*'}
    ))
    email_c = forms.EmailField(label="Email", required=True, widget=forms.EmailInput(
        attrs={'class':'form-control','placeholder':'Email*'}
    ))
    servicio = forms.ChoiceField(choices = SERVICIOS_DISPONIBLES, label="", initial='', widget=forms.Select(attrs={'class':'form-control'}), required=True)
