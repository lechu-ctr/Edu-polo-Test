from django import forms
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from validacion.validators import (validate_contraseña,validate_dni,
validate_domicilio,validate_fecha_nacimiento,validate_gmail,validate_genero,
validate_nombre_apellido,validate_telefono,validate_tutores)
#aca habria que importar los modelos para el sign in,persona,estudiante y usuario
#cabe aclarar no se su nombre
from 

class SignInForm(Forms,Form):
    dni=forms.CharField(
        label="DNI",
        max_length=9,
        validators=[validate_dni],
        widget=forms.TextInput(attrs={"placeholder":"123456789"})
    )
    nombre=forms.CharField(
        max_length=50,
        validators=[validate_nombre_apellido],
        widget=forms.TextInput(attrs={"placeholder":"nombre"})
    )
    correo=forms.EmailField(
        max_length=100,
        validators=[validate_gmail],
        widget=forms.EmailInput(attrs={"placeholder":"tu_correo@gmail.com"})
    )
    telefono=forms.CharField(
        max_length=11,
        validators=[validate_telefono],
        widget=forms.TextInput(attrs={"placeholder":"11223344556"})

    )
    fecha_nacimiento=forms.DateField(
        validators=[validate_fecha_nacimiento],
        widget=forms.DateInput(attrs={"placeholder":"date"})
    )
    genero=forms.ChoiceField(
        choices=[("Masculino","Masculino"),
                 ("Femenino","Femenino"),
                 ("Otro","Otro"),
                 ("Prefiero no decirlo","Prefiero no decirlo")
                 ],
        validators=[validate_genero]
    )
    domicilio=forms.CharField(
        max_length=150,
        required=False,
        validators=[validate_domicilio],
        widget=forms.TextInput(attrs={"placeholder":"domicilio(opcional)"})
    )
    condiciones_medicas=forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={"placeholder":"condiciones medicas(opcional)"})
    )

    contraseña=forms.CharField(
        label="contraseña",
        validators=[validate_contraseña],
        widget=forms.PasswordInput(attrs={"placeholder":"contraseña"})

    )
    confirmar_contraseña=forms.CharField(
        label="confirmar contraseña",
        validators=[validate_contraseña],
        widget=forms.PasswordInput(attrs={"placeholder":"repetir contraseña"})

    )
    permiso_imagen=forms.BooleanField(required=False)
    permiso_voz=forms.BooleanField(required=False)
    #llenar con choices de nivel de estudio
    nivel_estudios=forms

    institucion_actual=forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={"placeholder":"institucion actual"})
    )
    experiencia_laboral=forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={"placeholder":"experiencia laboral"})   
    )
    #revisar si no se usaban choices para las ciudad residencia
    ciudad_residencia=forms.CharField()
    
    def clean(self):
        cleaned_data= super().clean()
        contraseña=cleaned_data.get("contraseña")
        confirmar_contraseña =cleaned_data.get("confirmar_contraseña")
        if contraseña and confirmar_contraseña and contraseña != confirmar_contraseña:
            raise ValidationError("Las contraseñas no coinciden")
        
        dni=cleaned_data.get("dni")
        correo=cleaned_data.get("correo")
        #revisar que dni y correo no esten repetidos
