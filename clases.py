import os
import platform
def clear_console():
    os_name = platform.system()
    if os_name == "Windows":
        os.system('cls')
    else: # macOS o Linux
        os.system('clear')
        
class Paciente():
    def __init__(self, id, nombre, Apaterno, Amaterno, edad, sexo):
        self.id=id
        self.nombre=nombre
        self.Apaterno=Apaterno
        self.Amaterno=Amaterno
        self.edad=edad
        self.sexo=sexo
        
        self.activo=True
        
    def mostrarInfo():
        print()

class Expediente():
    def __init__(self, id, id_PACIENTE, Ant_Cancer, Ant_Diabetes):
        self.id=id
        self.id_PACIENTE=id_PACIENTE
        self.Alergias=[]
        self.Ant_Cancer=Ant_Cancer
        self.Ant_Diabetes=Ant_Diabetes
        
    def getAlergias(self):
        Alergias=[]
        aler=input("¿Tienes alguna alergia? 's' o 'n' ")
        
        if aler=='s' or aler=='S':
            opt=True
            while opt:
                alerTemp=input("Indica tu alergia: ")
                Alergias.append(alerTemp)
                optb=input("¿Tienes otra alergia? 's' o 'n' ")
                if optb=='s' or optb=='S':
                    opt=True
                else:
                    opt=False
                    
        if aler=='n' or aler=='N':
            Alergias[0]="Ninguna"
            
        self.Alergias=Alergias
        

class Insumos():
    def __init__(self, id, nombre, cantidad, costo):
        self.id=id
        self.nombre=nombre
        self.cantidad=cantidad
        self.costo=costo
    
class Operacion():
    def __init__(self, id, nombre, costMO, costTot):
        self.id=id
        self.nombre=nombre
        self.costMO=costMO
        self.costTot=costTot
        
class Historial():
    def __init__(self, id, id_PACIENTE, id_OPERACION):
        self.id=id
        self.id_PACIENTE=id_PACIENTE
        self.id_OPERACION=id_OPERACION
        