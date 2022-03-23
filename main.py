from clases import Paciente
from clases import Expediente
from clases import Insumos
from clases import Operacion
from clases import Historial
import os
import platform

def clear_console():
    os_name = platform.system()
    if os_name == "Windows":
        os.system('cls')
    else: # macOS o Linux
        os.system('clear')
        
#Hola wapo