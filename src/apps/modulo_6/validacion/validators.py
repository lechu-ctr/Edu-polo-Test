import re
from datetime import date
from django.core.exceptions import ValidationError
def validate_dni(value):
    v= str(value).strip()
    if not re.fullmatch(r'\d{9}',v):
        raise ValidationError("Dni invalido-Debe tener solo numeros y de 9 digitos")
    
def validate_nombre_apellido(value):
    v=str(value).strip()
    if not v:
        raise ValidationError("Este campo esta vacio")
    if not re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúÑñ\s'-]+",v):
        raise ValidationError("solo se permiten letras y espacios")
    
def validate_telefono(value):
    v=str(value).strip()
    if not re.fullmatch(r'\d{9,11}',v):
        raise ValidationError("solo de 9 a 11 letras")

def validate_gmail(value):
    v=str(email).strip().lower()
    if not e.endswith("@gmail.com"):
        raise ValidationError(Debe usar un correo que termine con @gmail.com)


def validate_fecha_nacimiento(value):
    if value> date.today():
        raise ValidationError("la fecha de nacimiento no puede ser futura")

def validate_domicilio(value):
    v=str(value).strip()
    if not v:
        raise ValidationError("El Domicilio no puede estar vacio")

def validate_tutores(value):

    edad = (date.today()- fecha_nacimiento).days//365

    cantidad_tutores= len(tutores) if tutores else 0
    if edad<16:
        if cantidad_tutores < 1:
            raise ValidationError("los menores de 16 años necesitan por lo menos 1 tutor registrado")

def validate_genero(value):
    opciones= ["Masculino","Femenino","Otro","Prefiero no decirlo"]
    if value not in opciones:
        raise ValidationError(f"el genero debe ser uno de los siguientes: {",".join(opciones)}.")
    


def validate_contraseña(value):
    if len(value)<8:
        raise ValidationError("La contraseña debe tener al menos 8 caracteres")
    if not re.search(r"[A-Z]",value):
        raise ValidationError("La contraseña debe tener al menos una letra mayuscula")
    if not re.search(r"[a-z]",value):
        raise ValidationError("La contraseña debe tener al menos una minuscula")
    if not re.search(r"\d", value):
        raise ValidationError("LA contraseña debe tener al menos un numero")
