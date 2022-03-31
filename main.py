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
        expedient.write(f'ALERGIA {i+1}: {Alergias[i]}, ')
    expedient.write(f'\nANT. CANCER: {Ant_Cancer}\n')
    expedient.write(f'ANT. DIABETES: {Ant_Diabetes}\n')
    expedient.close

def ver_expediente():
    print("¿DE QUE PACIENTE DESEA VER EXPEDIENTE?")
    for i in range (0,len(pacientes)):
        if pacientes[i][6] == True:
            print(f'{pacientes[i][0]}.- {pacientes[i][1]} {pacientes[i][2]} {pacientes[i][3]}')
    id_mos = input("INGRESA EL ID DE QUIEN DESEA VER EXPEDIENTE: ")
    clear_console()
    expediente = open(f"{id_mos}.txt", 'r')
    listita=[]
    for i in expediente:
        j = i
        t_n = j.replace("\n","")
        listita.append(t_n)
    print(f"----------EXPEDIENTE DE CLIENTE CON ID {id_mos}------------")
    for i in range (0, len(listita)-1):
        print(listita[i])
        print("----------------------")

#-------------------ID-NOMBRE INSUMO----CAJAS-PARES-PRECIO CAJA--GASTO ACUMULADO
guantes_desechables=[0,'GUANTE DESECHABLE',0, 0, 0,0]
guantes_quirurgicos = [1,'GUANTE QUIRURGICO',0,0,0,0]
mascarillas = [2,'MASCARILLAS',0,0,0,0]
baberos = [3,'BABEROS',0,0,0,0]
#jeringas-------------ID-NOMBRE INSUMO----CAJAS--CANTIDAD JERINGAS-PRECIO CAJA--GASTO ACUMULADO
jeringas = [4,'JERINGAS',0,0,0,0]
#anestesia------------ID-NOMBRE--CANTIDAD DE FRASCOS---MLporFRASCO---PRECIO FRASCO--GASTO ACUMULADO
anestesia=[5,'ANESTESIA',0,0,0,0]
insumos=[guantes_desechables,guantes_quirurgicos,mascarillas,baberos,jeringas,anestesia]

def alta_insumo():
    print("¿QUE INSUMO DESEA RESURTIR?")
    for i in range (0,len(insumos)):
        print(f'{i}.- {insumos[i][1]}')
    i_s = int(input('INGRESE EL ID DEL INSUMO A RESURTIR: '))
    insumo = Insumos(insumos[i_s][0],insumos[i_s][1],insumos[i_s][2],insumos[i_s][4])
    clear_console()
    print(f"-------RESURTIR {insumo.nombre}-----------")
    if i_s == 0:
        cajas = int(input('INGRESA EL NUMERO DE CAJAS ADQUIRIDAS: '))
        pares = int(input('INGRESA EL NUMERO DE PARES EN LA CAJA: '))
        precio = int(input('INGRESA EL PRECIO DE CADA CAJA: '))
        insumos[i_s][2] = insumo.cantidad + cajas
        insumos[i_s][3] = insumos[i_s][3] + pares
        insumos[i_s][4] = insumo.precio
        insumos[i_s][5] = insumo.precio + (precio * cajas)
    elif i_s == 1:
        cajas = int(input('INGRESA EL NUMERO DE CAJAS ADQUIRIDAS: '))
        pares = int(input('INGRESA EL NUMERO DE PARES EN LA CAJA: '))
        precio = int(input('INGRESA EL PRECIO DE CADA CAJA: '))
        insumos[i_s][2] = insumo.cantidad + cajas
        insumos[i_s][3] = insumos[i_s][3] + pares
        insumos[i_s][4] = insumo.precio
        insumos[i_s][5] = insumo.precio + (precio * cajas)
    elif i_s == 2:
        cajas = int(input('INGRESA EL NUMERO DE CAJAS ADQUIRIDAS: '))
        unidades = int(input('INGRESA EL NUMERO DE UNIDADES EN LA CAJA: '))
        precio = int(input('INGRESA EL PRECIO DE CADA CAJA: '))
        insumos[i_s][2] = insumo.cantidad + cajas
        insumos[i_s][3] = insumos[i_s][3] + unidades
        insumos[i_s][4] = insumo.precio
        insumos[i_s][5] = insumo.precio + (precio * cajas)
    elif i_s == 3:
        cajas = int(input('INGRESA EL NUMERO DE CAJAS ADQUIRIDAS: '))
        unidades = int(input('INGRESA EL NUMERO DE UNIDADES EN LA CAJA: '))
        precio = int(input('INGRESA EL PRECIO DE CADA CAJA: '))
        insumos[i_s][2] = insumo.cantidad + cajas
        insumos[i_s][3] = insumos[i_s][3] + unidades
        insumos[i_s][4] = insumo.precio
        insumos[i_s][5] = insumo.precio + (precio * cajas)
    elif i_s == 4:
        cajas = int(input('INGRESA EL NUMERO DE CAJAS ADQUIRIDAS: '))
        unidades = int(input('INGRESA EL NUMERO DE UNIDADES EN LA CAJA: '))
        precio = int(input('INGRESA EL PRECIO DE CADA CAJA: '))
        insumos[i_s][2] = insumo.cantidad + cajas
        insumos[i_s][3] = insumos[i_s][3] + unidades
        insumos[i_s][4] = insumo.precio
        insumos[i_s][5] = insumo.precio + (precio * cajas)
    elif i_s == 5:
        frascos = int(input('INGRESA EL FRASCOS ADQUIRIDOS: '))
        ml = int(input('INGRESA EL NUMERO DE MILILITROS POR FRASCO: '))
        precio = int(input('INGRESA EL PRECIO DE CADA FRASCO: '))
        insumos[i_s][2] = insumo.cantidad + cajas
        insumos[i_s][3] = insumos[i_s][3] + ml
        insumos[i_s][4] = insumo.precio
        insumos[i_s][5] = insumo.precio + (precio * frascos)
    

def menu():
    cont=True
    while cont:
        clear_console()
        print("1-Alta paciente")
        print("2-Habilitar paciente")
        print("3-Deshabilitar paciente")
        print("4-Ver expediente clínico")
        print("5-Alta insumo")
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
            ver_expediente()
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