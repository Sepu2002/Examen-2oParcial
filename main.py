from clases import Paciente
from clases import Expediente
from clases import Insumos
from clases import Operacion
from clases import Historial
import os
import platform

pacientes=[]
expedientes=[]

def clear_console():
    os_name = platform.system()
    if os_name == "Windows":
        os.system('cls')
    else: # macOS o Linux
        os.system('clear')
        
clear_console()
        
def alta_paciente():
    
    id=len(pacientes)
    nombre=input("Escriba el nombre de pila del paciente ")
    Apaterno=input("Escriba apellido paterno ")
    Amaterno=input("Escriba apellido materno ")
    edad=input("Escriba edad ")
    sexo=input("Escriba el sexo (M/F)")
    habilitado = True
    paciente=Paciente(id, nombre, Apaterno, Amaterno, edad, sexo)
    expediente = open(f"{id}.txt", 'a')
    expediente.write(f'ID PACIENTE: {paciente.id}\n')
    expediente.write(f'NOMBRE: {paciente.nombre} {paciente.Apaterno} {paciente.Amaterno}\n')
    expediente.write(f'EDAD: {paciente.edad}\n')
    expediente.write(f'SEXO: {paciente.sexo}\n')
    expediente.write(str(habilitado))
    expediente.close
    p=[id,nombre,Apaterno,Amaterno,edad,sexo,habilitado]
    pacientes.append(p)
    alta_expediente(id)

def habilitarPac ():
    print("¿QUE PACIENTE DESEA HABILITAR?")
    for i in range (0,len(pacientes)):
        if pacientes[i][6] == False:
            print(f'{pacientes[i][0]}.- {pacientes[i][1]} {pacientes[i][2]} {pacientes[i][3]}')
    id_mos = input("INGRESA EL ID DE QUIEN DESEAS HABILITAR: ")
    pacientes[int(id_mos)][6] = True
    input("PACIENTE HABILITADO EXITOSAMENTE ------- PRESIONA ENTER PARA CONTINUAR")

def deshabilitarPac ():
    print("¿QUE PACIENTE DESEA DESHABILITAR?")
    for i in range (0,len(pacientes)):
        if pacientes[i][6] == True:
            print(f'{pacientes[i][0]}.- {pacientes[i][1]} {pacientes[i][2]} {pacientes[i][3]}')
    id_mos = input("INGRESA EL ID DE QUIEN DESEAS DESHABILITAR: ")
    pacientes[int(id_mos)][6] = False
    input("PACIENTE DESHABILITADO EXITOSAMENTE ------- PRESIONA ENTER PARA CONTINUAR")

def getAlergias():
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
            Alergias.append("Ninguna")
            
        return Alergias
    
def alta_expediente(idpaciente):
    id=len(expedientes)
    idpac=idpaciente
    Alergias=getAlergias()
    Ant_Cancer=input("Tiene antecedente de cancer?  (S/N)")
    Ant_Diabetes=input("Tiene antecedente de diabetes= (S/N)")

    expediente=Expediente(id, idpac, Alergias, Ant_Cancer, Ant_Diabetes)
    e=[id, idpac, Alergias, Ant_Cancer, Ant_Diabetes]
    expedientes.append(e)
    expedient = open(f"{id}.txt", 'a')
    expedient.write(f'ID EXPEDIENTE: {expediente.id}\n')
    for i in range (0,len(Alergias)):
        expedient.write(f'ALERGIA {i+1}: {Alergias[i]}\n')
    expedient.write(f'ANT. CANCER: {Ant_Cancer}\n')
    expedient.write(f'ANT. DIABETES: {Ant_Diabetes}\n')
    expedient.close
def menu():
    cont=True
    while cont:
        clear_console()
        print("1-Alta paciente")
        print("2-Habilitar paciente")
        print("3-Deshabilitar paciente")
        #print("4-Ver expediente clínico")
        #print("5-Alta insumo")
        #print("6-Habilitar insumo")
        #print("7-Deshabilitar insumo")
        #print("8-Alta operación")
        #print("9-Habilitar operación")
        #print("10-Deshabilitar operación")
        #print("11-Ver historial de operaciones")
        print("12-Cerrar programa")
        
        opcion = int(input("OPCION ELEGIDA:  "))
        if opcion == 1: 
            clear_console()
            alta_paciente()
            input("OPRIMA ENTER PARA SALIR AL MENU")
        
        if opcion == 2: 
            clear_console()
            habilitarPac()
            input("OPRIMA ENTER PARA SALIR AL MENU")
        
        if opcion == 3: 
            clear_console()
            deshabilitarPac()
            input("OPRIMA ENTER PARA SALIR AL MENU")
        
        if opcion == 4: 
            clear_console()
        
            input("OPRIMA ENTER PARA SALIR AL MENU")
        
        if opcion == 5: 
            clear_console()
        
            input("OPRIMA ENTER PARA SALIR AL MENU")
            
        if opcion == 6:
            clear_console()
        
            input("OPRIMA ENTER PARA SALIR AL MENU")
            
        if opcion == 7: 
        
            input("OPRIMA ENTER PARA SALIR AL MENU")
            
        if opcion == 8: 
        
            input("OPRIMA ENTER PARA SALIR AL MENU")
            
        if opcion == 9: 
        
            input("OPRIMA ENTER PARA SALIR AL MENU")
            
        if opcion == 10: 
        
            input("OPRIMA ENTER PARA SALIR AL MENU")
            
        if opcion == 11: 
        
            input("OPRIMA ENTER PARA SALIR AL MENU")
            
        if opcion == 12: 
            cont=False
            input("OPRIMA ENTER PARA SALIR")
            
menu()
print(pacientes[0])
print(pacientes[1])
print(expedientes[0])  
print(expedientes[1]) 