#Este fichero contiene funciones auxiliares de uso general comunes

import re
import os
import platform


def limpiar_pantalla():
    """
    Function: Limpia la pantalla, 
    identificando el sistema operativo
    """    
    os.system ('cls') if platform.system() == "Windows" else os.system("clear")

def leer_texto(longitud_min=0,longitud_max=100,mensaje=None):
    print (mensaje) if mensaje else None
    while True:
        texto= input("> ")
        if len(texto)>=longitud_min and len(texto)<=longitud_max:
            return texto

#Validación del campo DNI
def dni_valido(dni, lista):
    if not re.match('[0-9]{2}[A-Z]$', dni):
        print ("DNI incorrecto, debe cumplir el formato.")
        return False
    for cliente in lista:
        if cliente.dni == dni:
            print ("DNI ya registrado.")
            return False
    return True

#Calculo de promedio de los estudiantes
def calculate_average(nota_1er_semestre, nota_2do_semestre):
    avg = sum([nota_1er_semestre, nota_2do_semestre]) / 2
    return avg

#Asignar la tecla "ENTER" a un button
def bind_enter_to_button(widget, button):
    def callback(event):
        button.invoke()
    widget.bind("<Return>", callback)


def center(root, width, height):
    """Centra la ventana en la pantalla"""
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    root.geometry(f"{width}x{height}+{x}+{y}")

