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


def validate(value):


def validate(value):