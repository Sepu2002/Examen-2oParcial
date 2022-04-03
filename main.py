from clases import Paciente
from clases import Expediente
from clases import Insumos
from clases import Operacion
from clases import Historial
import os
import platform

pacientes=[]
expedientes=[]
operaciones=[]
operaciones_con_nombre=[]
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
    habilitado = 'True'
    paciente=Paciente(id, nombre, Apaterno, Amaterno, edad, sexo)
    expediente = open(f"{id}.txt", 'a')
    expediente.write(f'ID PACIENTE: {paciente.id}\n')
    expediente.write(f'NOMBRE: {paciente.nombre} {paciente.Apaterno} {paciente.Amaterno}\n')
    expediente.write(f'EDAD: {paciente.edad}\n')
    expediente.write(f'SEXO: {paciente.sexo}\n')
    expediente.write(str(habilitado))
    expediente.close
    expediente = open(f"{id}_lista.txt", 'a')
    expediente.write(f'{paciente.id}\n')
    expediente.write(f'{paciente.nombre}\n')
    expediente.write(f'{paciente.Apaterno}\n')
    expediente.write(f'{paciente.Amaterno}\n')
    expediente.write(f'{paciente.edad}\n')
    expediente.write(f'{paciente.sexo}\n')
    expediente.write(str(habilitado))
    expediente.close
    p=[id,nombre,Apaterno,Amaterno,edad,sexo,habilitado]
    pacientes.append(p)
    alta_expediente(id)
    idPacientesGeneral = open('ID_PACIENTES.txt', 'a')
    idPacientesGeneral.write(f'{id}\n')
    idPacientesGeneral.close
    archivo = open(f'Operaciones_{paciente.id}.txt', 'a')
    archivo_aportacion = open(f'APORTACION_{paciente.id}.txt','a')
    archivo.close
    archivo_aportacion.close

def leer_pacientes():
    idgeneral = open('ID_PACIENTES.txt', 'r')
    for i in idgeneral:
        p =[]
        j = i
        t = j.replace("\n","")
        idpaciente = open(f'{t}_lista.txt', 'r')
        for a in idpaciente:
            j = a
            t_n = j.replace("\n","")
            p.append(str(t_n))
        idpaciente.close
        pacientes.append(p)
    idgeneral.close


def habilitarPac ():
    print("¿QUE PACIENTE DESEA HABILITAR?")
    for i in range (0,len(pacientes)):
        if pacientes[i][6] == 'False':
            print(f'{pacientes[i][0]}.- {pacientes[i][1]} {pacientes[i][2]} {pacientes[i][3]}')
    id_mos = int(input("INGRESA EL ID DE QUIEN DESEAS HABILITAR: "))
    pacientes[int(id_mos)][6] = 'True'
    expediente = open(f"{id_mos}_lista.txt", 'w')
    expediente.write(f'{pacientes[id_mos][0]}\n')
    expediente.write(f'{pacientes[id_mos][1]}\n')
    expediente.write(f'{pacientes[id_mos][2]}\n')
    expediente.write(f'{pacientes[id_mos][3]}\n')
    expediente.write(f'{pacientes[id_mos][4]}\n')
    expediente.write(f'{pacientes[id_mos][5]}\n')
    expediente.write(str(pacientes[id_mos][6]))
    expediente.close
    input("PACIENTE HABILITADO EXITOSAMENTE ------- PRESIONA ENTER PARA CONTINUAR")

def deshabilitarPac ():
    print("¿QUE PACIENTE DESEA DESHABILITAR?")
    for i in range (0,len(pacientes)):
        if pacientes[i][6] == 'True':
            print(f'{pacientes[i][0]}.- {pacientes[i][1]} {pacientes[i][2]} {pacientes[i][3]}')
    id_mos = int(input("INGRESA EL ID DE QUIEN DESEAS DESHABILITAR: "))
    pacientes[int(id_mos)][6] = 'False'
    expediente = open(f"{id_mos}_lista.txt", 'w')
    expediente.write(f'{pacientes[id_mos][0]}\n')
    expediente.write(f'{pacientes[id_mos][1]}\n')
    expediente.write(f'{pacientes[id_mos][2]}\n')
    expediente.write(f'{pacientes[id_mos][3]}\n')
    expediente.write(f'{pacientes[id_mos][4]}\n')
    expediente.write(f'{pacientes[id_mos][5]}\n')
    expediente.write(str(pacientes[id_mos][6]))
    expediente.close
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
    expedient = open(f"{idpac}.txt", 'a')
    expedient.write(f'\nID EXPEDIENTE: {expediente.id}\n')
    for i in range (0,len(Alergias)):
        expedient.write(f'ALERGIA {i+1}: {Alergias[i]}, ')
    expedient.write(f'\nANT. CANCER: {Ant_Cancer}\n')
    expedient.write(f'ANT. DIABETES: {Ant_Diabetes}')
    expedient.close

def ver_expediente():
    print("¿DE QUE PACIENTE DESEA VER EXPEDIENTE?")
    for i in range (0,len(pacientes)):
        if pacientes[i][6] == 'True':
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
    for i in range (0, len(listita)):
        if i < 4 or i > 4:
            print(listita[i])
            print("----------------------")

def leer_insumos_predert():
    insunuevos = open("insumosNuevos.txt",'r')
    for o in insunuevos:
        a = o
        r = a.replace("\n","")
        idgeneral = open(f'{int(r)}_insumo.txt', 'r')
        p =[]
        for i in idgeneral:
            j = i
            t = j.replace("\n","")
            p.append(t)
        insumos[int(r)] = p
        idgeneral.close
#-------------------ID-NOMBRE INSUMO----CAJAS-PARES-PRECIO CAJA--GASTO ACUMULADO
guantes_desechables=[0,'GUANTE DESECHABLE',0, 0, 0,0,1]
guantes_quirurgicos = [1,'GUANTE QUIRURGICO',0,0,0,0,1]
mascarillas = [2,'MASCARILLAS',0,0,0,0,1]
baberos = [3,'BABEROS',0,0,0,0,1]
#jeringas-------------ID-NOMBRE INSUMO----CAJAS--CANTIDAD JERINGAS-PRECIO CAJA--GASTO ACUMULADO
jeringas = [4,'JERINGAS',0,0,0,0,1]
#anestesia------------ID-NOMBRE--CANTIDAD DE FRASCOS---MLporFRASCO---PRECIO FRASCO--GASTO ACUMULADO
anestesia=[5,'ANESTESIA',0,0,0,0,1]
insumo0 = open(f'{0}_insumo.txt', 'a')
insumo1 = open(f'{1}_insumo.txt', 'a')
insumo2 = open(f'{2}_insumo.txt', 'a')
insumo3 = open(f'{3}_insumo.txt', 'a')
insumo4 = open(f'{4}_insumo.txt', 'a')
insumo5 = open(f'{5}_insumo.txt', 'a')
insumo0.close
insumo1.close
insumo2.close
insumo3.close
insumo4.close
insumo5.close
insumos=[guantes_desechables,guantes_quirurgicos,mascarillas,baberos,jeringas,anestesia]

def escribir_archivo_insumos(id, nombre, cajas, unidades, precio, acumulado, activacion):
    insumo = open(f'{id}_insumo.txt', 'w')
    insumo.write(f'{id}\n')
    insumo.write(f'{nombre}\n')
    insumo.write(f'{cajas}\n')
    insumo.write(f'{unidades}\n')
    insumo.write(f'{precio}\n')
    insumo.write(f'{acumulado}\n')
    insumo.write(f'{activacion}')
    insumo.close

def gastos_general(costo):
    gastos_engeneral = open('Gastos_Insumos.txt','r')
    gastos = 0
    for i in gastos_engeneral:
        gastos = float(i)
    gastos_engeneral.close
    gastos_engeneralw = open('Gastos_Insumos.txt','w')
    gastos_engeneralw.write(f'{gastos+costo}')
    gastos_engeneralw.close

def alta_insumo():
    print("¿QUE INSUMO DESEA RESURTIR?")
    for i in range (0,len(insumos)):
        if int(insumos[i][6]) == 1:
            print(f'{i}.- {insumos[i][1]}')
    i_s = int(input('INGRESE EL ID DEL INSUMO A RESURTIR: '))
    insumo = Insumos(insumos[i_s][0],insumos[i_s][1],float(insumos[i_s][2]),float(insumos[i_s][5]))
    clear_console()
    print(f"-------RESURTIR {insumo.nombre}-----------")
    if i_s == 0:
        cajas = float(input('INGRESA EL NUMERO DE CAJAS ADQUIRIDAS: '))
        pares = float(input('INGRESA EL NUMERO DE PARES EN LA CAJA: '))
        precio = float(input('INGRESA EL PRECIO DE CADA CAJA: '))
        insumos[i_s][2] = insumo.cantidad + cajas
        insumos[i_s][3] = float(insumos[i_s][3]) + (pares*cajas)
        insumos[i_s][4] = precio
        insumos[i_s][5] = insumo.costo + (precio * cajas)
        escribir_archivo_insumos(i_s, insumos[i_s][1], insumos[i_s][2], insumos[i_s][3], insumos[i_s][4], insumos[i_s][5], insumos[i_s][6])
        insunuevos = open("insumosNuevos.txt",'a')
        insunuevos.write(f'{insumos[i_s][0]}\n')
        insunuevos.close
        gastos_general(precio * cajas)
    elif i_s == 1:
        cajas = float(input('INGRESA EL NUMERO DE CAJAS ADQUIRIDAS: '))
        pares = float(input('INGRESA EL NUMERO DE PARES EN LA CAJA: '))
        precio = float(input('INGRESA EL PRECIO DE CADA CAJA: '))
        insumos[i_s][2] = insumo.cantidad + cajas
        insumos[i_s][3] = float(insumos[i_s][3]) + (pares*cajas)
        insumos[i_s][4] = precio
        insumos[i_s][5] = insumo.costo + (precio * cajas)
        escribir_archivo_insumos(i_s, insumos[i_s][1], insumos[i_s][2], insumos[i_s][3], insumos[i_s][4], insumos[i_s][5], insumos[i_s][6])
        insunuevos = open("insumosNuevos.txt",'a')
        insunuevos.write(f'{insumos[i_s][0]}\n')
        insunuevos.close
        gastos_general(precio * cajas)
    elif i_s == 2:
        cajas = float(input('INGRESA EL NUMERO DE CAJAS ADQUIRIDAS: '))
        unidades = float(input('INGRESA EL NUMERO DE UNIDADES EN LA CAJA: '))
        precio = float(input('INGRESA EL PRECIO DE CADA CAJA: '))
        insumos[i_s][2] = insumo.cantidad + cajas
        insumos[i_s][3] = float(insumos[i_s][3]) + (unidades*cajas)
        insumos[i_s][4] = precio
        insumos[i_s][5] = insumo.costo + (precio * cajas)
        escribir_archivo_insumos(i_s, insumos[i_s][1], insumos[i_s][2], insumos[i_s][3], insumos[i_s][4], insumos[i_s][5], insumos[i_s][6])
        insunuevos = open("insumosNuevos.txt",'a')
        insunuevos.write(f'{insumos[i_s][0]}\n')
        insunuevos.close
        gastos_general(precio * cajas)
    elif i_s == 3:
        cajas = float(input('INGRESA EL NUMERO DE CAJAS ADQUIRIDAS: '))
        unidades = float(input('INGRESA EL NUMERO DE UNIDADES EN LA CAJA: '))
        precio = float(input('INGRESA EL PRECIO DE CADA CAJA: '))
        insumos[i_s][2] = insumo.cantidad + cajas
        insumos[i_s][3] = float(insumos[i_s][3]) + (unidades*cajas)
        insumos[i_s][4] = precio
        insumos[i_s][5] = insumo.costo + (precio * cajas)
        escribir_archivo_insumos(i_s, insumos[i_s][1], insumos[i_s][2], insumos[i_s][3], insumos[i_s][4], insumos[i_s][5], insumos[i_s][6])
        insunuevos = open("insumosNuevos.txt",'a')
        insunuevos.write(f'{insumos[i_s][0]}\n')
        insunuevos.close
        gastos_general(precio * cajas)
    elif i_s == 4:
        cajas = float(input('INGRESA EL NUMERO DE CAJAS ADQUIRIDAS: '))
        unidades = float(input('INGRESA EL NUMERO DE UNIDADES EN LA CAJA: '))
        precio = float(input('INGRESA EL PRECIO DE CADA CAJA: '))
        insumos[i_s][2] = insumo.cantidad + cajas
        insumos[i_s][3] = float(insumos[i_s][3]) + (unidades*cajas)
        insumos[i_s][4] = precio
        insumos[i_s][5] = insumo.costo + (precio * cajas)
        escribir_archivo_insumos(i_s, insumos[i_s][1], insumos[i_s][2], insumos[i_s][3], insumos[i_s][4], insumos[i_s][5], insumos[i_s][6])
        insunuevos = open("insumosNuevos.txt",'a')
        insunuevos.write(f'{insumos[i_s][0]}\n')
        insunuevos.close
        gastos_general(precio * cajas)
    elif i_s == 5:
        frascos = float(input('INGRESA EL FRASCOS ADQUIRIDOS: '))
        ml = float(input('INGRESA EL NUMERO DE MILILITROS POR FRASCO: '))
        precio = float(input('INGRESA EL PRECIO DE CADA FRASCO: '))
        insumos[i_s][2] = insumo.cantidad + frascos
        insumos[i_s][3] = float(insumos[i_s][3]) + (ml*frascos)
        insumos[i_s][4] = precio
        insumos[i_s][5] = insumo.costo + (precio * frascos)
        escribir_archivo_insumos(i_s, insumos[i_s][1], insumos[i_s][2], insumos[i_s][3], insumos[i_s][4], insumos[i_s][5], insumos[i_s][6])
        insunuevos = open("insumosNuevos.txt",'a')
        insunuevos.write(f'{insumos[i_s][0]}\n')
        insunuevos.close
        gastos_general(precio * frascos)
    elif i_s > 5 and i_s < len(insumos):
        cajas = float(input('INGRESA EL NUMERO DE CAJAS ADQUIRIDAS: '))
        unidades = float(input('INGRESA EL NUMERO DE UNIDADES EN LA CAJA: '))
        precio = float(input('INGRESA EL PRECIO DE CADA CAJA: '))
        insumos[i_s][2] = insumo.cantidad + cajas
        insumos[i_s][3] = float(insumos[i_s][3]) + (unidades*cajas)
        insumos[i_s][4] = precio
        insumos[i_s][5] = insumo.costo + (precio * cajas)
        escribir_archivo_insumos(i_s, insumos[i_s][1], insumos[i_s][2], insumos[i_s][3], insumos[i_s][4], insumos[i_s][5], insumos[i_s][6])
        insunuevos = open("insumosNuevos.txt",'a')
        insunuevos.write(f'{insumos[i_s][0]}\n')
        insunuevos.close
        gastos_general(precio * cajas)

    clear_console()
    print('.....................................................RESUMEN DE INSUMOS..................................................................................')
    print('|   ID    |   INSUMO   |   CAJAS/FRASCOS ACUMULADOS   |   UNIDADES TOTALES  |   PRECIO CAJA/FRASCO ULTIMO   |   COSTO DE LAS UNIDADES EN EXISTENCIA   |')
    for i in range (0, len(insumos)):
        if int(insumos[i][6]) == 1:
            print('......................................................................................................................................................')
            print(f'|     {insumos[i][0]}     |     {insumos[i][1]}     |     {insumos[i][2]}     |     {insumos[i][3]}     |     {insumos[i][4]}     |     {insumos[i][5]}     |')
    print('......................................................................................................................................................')

def ver_insumos():
    clear_console()
    print('.....................................................RESUMEN DE INSUMOS..................................................................................')
    print('|   ID    |   INSUMO   |   CAJAS/FRASCOS ACUMULADOS   |   UNIDADES TOTALES  |   PRECIO CAJA/FRASCO ULTIMO   |   COSTO DE LAS UNIDADES EN EXISTENCIA   |')
    for i in range (0, len(insumos)):
        if int(insumos[i][6]) == 1:
            print('......................................................................................................................................................')
            print(f'|   {insumos[i][0]}     |     {insumos[i][1]}     |     {insumos[i][2]}     |     {insumos[i][3]}     |     {insumos[i][4]}     |     {insumos[i][5]}     |')
    print('......................................................................................................................................................')

def habilitar_insumo():
    nombre = str(input('INGRESA EL NOMBRE DEL INSUMO: '))
    cajas = float(input('INGRESA EL NUMERO DE CAJAS ADQUIRIDAS: '))
    unidades = float(input('INGRESA EL NUMERO DE UNIDADES EN LA CAJA: '))
    precio = float(input('INGRESA EL PRECIO DE CADA CAJA: '))
    id = len(insumos)
    listalocal =[id,nombre,cajas,(unidades*cajas),precio,(precio*cajas),1]
    insunuevos = open("insumosNuevos.txt",'a')
    insunuevos.write(f'{id} \n')
    insunuevos.close
    insumos.append(listalocal)
    listatamano = open('tamalista.txt', 'w')
    listatamano.write(f'{len(insumos)}')
    listatamano.close
    insumo = open(f'{id}_insumo.txt', 'a')
    insumo.write(f'{id}\n')
    insumo.write(f'{nombre}\n')
    insumo.write(f'{cajas}\n')
    insumo.write(f'{unidades*cajas}\n')
    insumo.write(f'{precio}\n')
    insumo.write(f'{listalocal[5]}\n')
    insumo.write(f'1')
    insumo.close
    gastos_general(precio * cajas)

def inactivar():
    print("¿QUE INSUMO DESEA INACTIVAR?")
    for i in range (0,len(insumos)):
        if int(insumos[i][6]) == 1:
            print(f'{i}.- {insumos[i][1]}')
    i_s = int(input('INGRESE EL ID DEL INSUMO A INACTIVAR: '))
    insumos[i_s][6] = 0
    escribir_archivo_insumos(i_s, insumos[i_s][1], insumos[i_s][2], insumos[i_s][3], insumos[i_s][4], insumos[i_s][5], insumos[i_s][6])

def activar():
    print("¿QUE INSUMO DESEA ACTIVAR?")
    for i in range (0,len(insumos)):
        if int(insumos[i][6]) == 0:
            print(f'{i}.- {insumos[i][1]}')
    i_s = int(input('INGRESE EL ID DEL INSUMO A ACTIVAR: '))
    insumos[i_s][6] = 1
    escribir_archivo_insumos(i_s, insumos[i_s][1], insumos[i_s][2], insumos[i_s][3], insumos[i_s][4], insumos[i_s][5], insumos[i_s][6])

def alta_operacion():
    insumos_operacion=[]
    costo_materiales = 0
    print("¿A QUE PACIENTE REALIZARÁ LA OPERACIÓN?")
    for i in range (0,len(pacientes)):
        if pacientes[i][6] == 'True':
            print(f'{pacientes[i][0]}.- {pacientes[i][1]} {pacientes[i][2]} {pacientes[i][3]}')
    id_mos = input("INGRESA EL ID DE CLIENTE: ")
    clear_console()
    tipo = str(input('INGRESE EL TIPO DE OPERACIÓN QUE REALIZARÁ: '))
    mo = float(input('INDICA EL COSTO DE MANO DE OBRA DE ESTE PROCEDIMIENTO: '))
    clear_console()
    print('¿QUE INSUMOS UTILIZARÁ?')
    ver_insumos()
    a = True
    f = str(input('UTILIZARÁ ALGUN INSUMO? (s/n): '))
    while a:
        clear_console()
        ver_insumos()
        if f == "s" or f == 'S':
            i_s = int(input('INGRESA EL ID DEL INSUMO A UTILIZAR: '))
            insumo = Insumos(insumos[i_s][0],insumos[i_s][1],float(insumos[i_s][2]),float(insumos[i_s][5]))
            clear_console()
            print(f"-------UTILIZAR {insumo.nombre}-----------")
            insumo_pro = []
            if i_s == 0:
                pares = float(input('INGRESA EL NUMERO DE PARES A UTILIZAR: '))
                if pares > float(insumos[i_s][3]):
                    print('NO CUENTAS CON LA CANTIDAD SUFICIENTE DE UNIDADES DE ESTE INSUMO')
                    input('SERÁ REGRESADO AL MENÚ PRINCIPAL PARA REABASTECER SUS INSUMOS -OPRIMA ENTER- ')
                    f = 'n'
                    break
                else: 
                    costo_insumo = ((float(insumos[i_s][5]) / float(insumos[i_s][3])) * pares)
                    insumos[i_s][5] = insumo.costo - costo_insumo
                    insumos[i_s][3] = float(insumos[i_s][3]) - pares
                    escribir_archivo_insumos(i_s, insumos[i_s][1], insumos[i_s][2], insumos[i_s][3], insumos[i_s][4], insumos[i_s][5], insumos[i_s][6])
                    insumo_pro = [insumos[i_s][0], insumos[i_s][1],pares]
                    insumos_operacion.append(insumo_pro)
                    costo_materiales = costo_materiales + costo_insumo
                    f = str(input('UTILIZARÁ ALGUN OTRO INSUMO? (s/n): '))
                
            elif i_s == 1:
                pares = float(input('INGRESA EL NUMERO DE PARES A UTILIZAR: '))
                if pares > float(insumos[i_s][3]):
                    print('NO CUENTAS CON LA CANTIDAD SUFICIENTE DE UNIDADES DE ESTE INSUMO')
                    input('SERÁ REGRESADO AL MENÚ PRINCIPAL PARA REABASTECER SUS INSUMOS -OPRIMA ENTER- ')
                    f = 'n'
                    break
                else:
                    costo_insumo = ((float(insumos[i_s][5]) / float(insumos[i_s][3])) * pares)
                    insumos[i_s][5] = insumo.costo - costo_insumo
                    insumos[i_s][3] = float(insumos[i_s][3]) - pares
                    escribir_archivo_insumos(i_s, insumos[i_s][1], insumos[i_s][2], insumos[i_s][3], insumos[i_s][4], insumos[i_s][5], insumos[i_s][6])
                    insumo_pro = [insumos[i_s][0], insumos[i_s][1],pares]
                    insumos_operacion.append(insumo_pro)
                    costo_materiales = costo_materiales + costo_insumo
                    f = str(input('UTILIZARÁ ALGUN OTRO INSUMO? (s/n): '))
                
            elif i_s == 2:
                pares = float(input('INGRESA EL NUMERO DE MASCARILLAS: '))
                if pares > float(insumos[i_s][3]):
                    print('NO CUENTAS CON LA CANTIDAD SUFICIENTE DE UNIDADES DE ESTE INSUMO')
                    input('SERÁ REGRESADO AL MENÚ PRINCIPAL PARA REABASTECER SUS INSUMOS -OPRIMA ENTER- ')
                    f = 'n'
                    break
                else:
                    costo_insumo = ((float(insumos[i_s][5]) / float(insumos[i_s][3])) * pares)
                    insumos[i_s][5] = insumo.costo - costo_insumo
                    insumos[i_s][3] = float(insumos[i_s][3]) - pares
                    escribir_archivo_insumos(i_s, insumos[i_s][1], insumos[i_s][2], insumos[i_s][3], insumos[i_s][4], insumos[i_s][5], insumos[i_s][6])
                    insumo_pro = [insumos[i_s][0], insumos[i_s][1],pares]
                    insumos_operacion.append(insumo_pro)
                    costo_materiales = costo_materiales + costo_insumo
                    f = str(input('UTILIZARÁ ALGUN OTRO INSUMO? (s/n): '))
                
            elif i_s == 3:
                pares = float(input('INGRESA EL NUMERO DE BABEROS A UTILIZAR: '))
                if pares > float(insumos[i_s][3]):
                    print('NO CUENTAS CON LA CANTIDAD SUFICIENTE DE UNIDADES DE ESTE INSUMO')
                    input('SERÁ REGRESADO AL MENÚ PRINCIPAL PARA REABASTECER SUS INSUMOS -OPRIMA ENTER- ')
                    f = 'n'
                    break
                else:
                    costo_insumo = ((float(insumos[i_s][5]) / float(insumos[i_s][3])) * pares)
                    insumos[i_s][5] = insumo.costo - costo_insumo
                    insumos[i_s][3] = float(insumos[i_s][3]) - pares
                    escribir_archivo_insumos(i_s, insumos[i_s][1], insumos[i_s][2], insumos[i_s][3], insumos[i_s][4], insumos[i_s][5], insumos[i_s][6])
                    insumo_pro = [insumos[i_s][0], insumos[i_s][1],pares]
                    insumos_operacion.append(insumo_pro)
                    costo_materiales = costo_materiales + costo_insumo
                    f = str(input('UTILIZARÁ ALGUN OTRO INSUMO? (s/n): '))
                
            elif i_s == 4:
                pares = float(input('INGRESA EL NUMERO DE JERINGAS: '))
                if pares > float(insumos[i_s][3]):
                    print('NO CUENTAS CON LA CANTIDAD SUFICIENTE DE UNIDADES DE ESTE INSUMO')
                    input('SERÁ REGRESADO AL MENÚ PRINCIPAL PARA REABASTECER SUS INSUMOS -OPRIMA ENTER- ')
                    f = 'n'
                    break
                else:
                    costo_insumo = ((float(insumos[i_s][5]) / float(insumos[i_s][3])) * pares)
                    insumos[i_s][5] = insumo.costo - costo_insumo
                    insumos[i_s][3] = float(insumos[i_s][3]) - pares
                    escribir_archivo_insumos(i_s, insumos[i_s][1], insumos[i_s][2], insumos[i_s][3], insumos[i_s][4], insumos[i_s][5], insumos[i_s][6])
                    insumo_pro = [insumos[i_s][0], insumos[i_s][1],pares]
                    insumos_operacion.append(insumo_pro)
                    costo_materiales = costo_materiales + costo_insumo
                    f = str(input('UTILIZARÁ ALGUN OTRO INSUMO? (s/n): '))
                
            elif i_s == 5:
                pares = float(input('INGRESA EL NUMERO DE MILILITROS DE ANESTESIA A UTILIZAR: '))
                if pares > float(insumos[i_s][3]):
                    print('NO CUENTAS CON LA CANTIDAD SUFICIENTE DE UNIDADES DE ESTE INSUMO')
                    input('SERÁ REGRESADO AL MENÚ PRINCIPAL PARA REABASTECER SUS INSUMOS -OPRIMA ENTER- ')
                    f = 'n'
                    break
                else:
                    costo_insumo = ((float(insumos[i_s][5]) / float(insumos[i_s][3])) * pares)
                    insumos[i_s][5] = insumo.costo - costo_insumo
                    insumos[i_s][3] = float(insumos[i_s][3]) - pares
                    escribir_archivo_insumos(i_s, insumos[i_s][1], insumos[i_s][2], insumos[i_s][3], insumos[i_s][4], insumos[i_s][5], insumos[i_s][6])
                    insumo_pro = [insumos[i_s][0], insumos[i_s][1],pares]
                    insumos_operacion.append(insumo_pro)
                    costo_materiales = costo_materiales + costo_insumo
                    f = str(input('UTILIZARÁ ALGUN OTRO INSUMO? (s/n): '))
                
            elif i_s > 5 and i_s < len(insumos):
                pares = float(input('INGRESA EL NUMERO DE UNIDADES A UTILIZAR: '))
                if pares > float(insumos[i_s][3]):
                    print('NO CUENTAS CON LA CANTIDAD SUFICIENTE DE UNIDADES DE ESTE INSUMO')
                    input('SERÁ REGRESADO AL MENÚ PRINCIPAL PARA REABASTECER SUS INSUMOS -OPRIMA ENTER- ')
                    f = 'n'
                    break
                else:
                    costo_insumo = ((float(insumos[i_s][5]) / float(insumos[i_s][3])) * pares)
                    insumos[i_s][5] = insumo.costo - costo_insumo
                    insumos[i_s][3] = float(insumos[i_s][3]) - pares
                    escribir_archivo_insumos(i_s, insumos[i_s][1], insumos[i_s][2], insumos[i_s][3], insumos[i_s][4], insumos[i_s][5], insumos[i_s][6])
                    insumo_pro = [insumos[i_s][0], insumos[i_s][1],pares]
                    insumos_operacion.append(insumo_pro)
                    costo_materiales = costo_materiales + costo_insumo
                    f = str(input('UTILIZARÁ ALGUN OTRO INSUMO? (s/n): '))
            

        else:
            data_operación = Operacion(len(operaciones),tipo,mo,(mo+costo_materiales))
            numerooperaciones = open('NUMERO_OPERACIONES.txt','a')
            numerooperaciones.write(f'{len(operaciones)}\n')
            numerooperaciones.close
            numerooperaciones = open('NUMERO_OPERACIONES_USUARIO.txt','a')
            numerooperaciones.write(f'{id_mos}\n')
            numerooperaciones.close
            op = [data_operación.id, id_mos]
            nombre = (f'{pacientes[int(id_mos)][1]} {pacientes[int(id_mos)][2]} {pacientes[int(id_mos)][3]}')
            operdatos = [data_operación.id,id_mos, nombre]
            operaciones_con_nombre.append(operdatos)
            operaciones.append(op)
            archivooper = open(f'OPERACION_{id_mos}_{data_operación.id}.txt', 'a')
            archivooper.write(f'ID OPERACIÓN: {data_operación.id}\n')
            archivooper.write(f'PROCEDIMIENTO REALIZADO: {tipo}\n')
            archivooper.write(f'CLIENTE A QUIEN SE LE REALIZO: {pacientes[int(id_mos)][1]} {pacientes[int(id_mos)][2]} {pacientes[int(id_mos)][3]}\n')
            archivooper.write(f'MANO DE OBRA: ${mo}\n')
            archivooper.write(f'COSTO MATERIALES: ${costo_materiales}\n')
            archivooper.write(f'COSTO TOTAL OPERACIÓN: ${data_operación.costTot}\n')
            for i in range (0, len(insumos_operacion)):
                archivooper.write(f'ID INSUMO: {insumos_operacion[i][0]} | NOMBRE DEL INSUMO: {insumos_operacion[i][1]} | UNIDADES UTILIZADAS: {insumos_operacion[i][2]}\n')
            archivooper.close
            ingresos = open('INGRESOS.txt','r')
            ganancia_parcial = 0
            for i in ingresos:
                ganancia_parcial = float(i)
            ingresos.close
            ingresosw = open('INGRESOS.txt','w')
            ingresosw.write(f'{ganancia_parcial+mo}')
            
            ingresos = open('GASTOS.txt','r')
            ganancia_parcial = 0
            for i in ingresos:
                ganancia_parcial = float(i)
            ingresos.close
            ingresosw = open('GASTOS.txt','w')
            ingresosw.write(f'{ganancia_parcial+costo_materiales}')
            historialoperaciones = open('Hist_Oper.txt','a')
            historialoperaciones.write(f'ID OPERACIÓN: {data_operación.id} | PROCEDIMIENTO REALIZADO: {tipo} | CLIENTE: {pacientes[int(id_mos)][1]} {pacientes[int(id_mos)][2]} {pacientes[int(id_mos)][3]} | COSTO OPERACIÓN: ${data_operación.costTot}\n')
            historialoperaciones.close
            archivo_operaciones_por_paciente = open(f'Operaciones_{id_mos}.txt','a')
            archivo_operaciones_por_paciente.write(f'ID OPERACIÓN: {data_operación.id} | PROCEDIMIENTO REALIZADO: {tipo} | COSTO OPERACIÓN: ${data_operación.costTot}\n')
            archivo_operaciones_por_paciente.close
            archivo_aportación = open(f'APORTACION_{id_mos}.txt','a')
            archivo_aportación.close
        
            archivo_aportación = open(f'APORTACION_{id_mos}.txt','r')
            ap_parcial = 0
            for i in archivo_aportación:
                ap_parcial = float(i)
            archivo_aportación.close
            apw = open(f'APORTACION_{id_mos}.txt','w')
            apw.write(f'{ap_parcial+data_operación.costTot}')
            a = False

def lectura_operaciones():
    idOperGen = open('NUMERO_OPERACIONES.txt', 'r')
    p =[]
    q = []
    
    for i in idOperGen:
        j = i
        t = j.replace("\n","")
        p.append(int(t))
    
    idpacienteOper = open(f'NUMERO_OPERACIONES_USUARIO.txt', 'r')
    for a in idpacienteOper:
        j = a
        t_n = j.replace("\n","")
        q.append(int(t_n))
    idpacienteOper.close
    idOperGen.close
    for i in range (0,len(p)):
        ids =[0,0]
        ids[0] = p[i]
        ids[1] = q[i]
        operaciones.append(ids)
        k = [ids[0],ids[1],f'{pacientes[ids[1]][1]} {pacientes[ids[1]][2]} {pacientes[ids[1]][3]}']
        operaciones_con_nombre.append(k)
def ver_historial_operaciones():
    hist = open('Hist_Oper.txt','r')
    for i in hist:
        j = i
        t = j.replace("\n","")
        print(t)
    hist.close

def ver_hist_pacientes():
    if len(operaciones_con_nombre) != 0:
        print("OPERACIONES DE LAS CUALES SE PUEDE HACER CONSULTA")
        for i in range (0,len(operaciones_con_nombre)):
            print(f'{i}.- ID OPERACION: {operaciones_con_nombre[i][0]} | ID CLIENTE: {operaciones_con_nombre[i][1]} | NOMBRE CLIENTE: {operaciones_con_nombre[i][2]}')
        a = int(input('ESCRIBE EL ID DE LISTA PARA MÁS INFORMACIÓN (ej. 1.-): '))
        clear_console()
        histor = Historial(operaciones_con_nombre[a][1], operaciones_con_nombre[a][0])
        archivooper = open(f'OPERACION_{histor.id_PACIENTE}_{histor.id_OPERACION}.txt', 'r')
        for i in archivooper:
            j = i
            t = j.replace("\n","")
            print(t)
        archivooper.close
    else:
        print('AUN NO SE HAN REALIZADO OPERACIONES')

def operaciones_paciente():
    print("¿DE QUE PACIENTE DESEA VER SU INFORMACIÓN DE APORTACIONES Y OPERACIONES?")
    for i in range (0,len(pacientes)):
        if pacientes[i][6] == 'True':
            print(f'{pacientes[i][0]}.- {pacientes[i][1]} {pacientes[i][2]} {pacientes[i][3]}')
    id_mos = int(input("INGRESA EL ID DE CLIENTE: "))
    clear_console()
    archivo = open(f'Operaciones_{id_mos}.txt', 'r')
    conteo_operaciones = 0
    for d in archivo:
        j = d
        t = j.replace("\n","")
        conteo_operaciones+=1
        print(t)
    print('----------------------------------------------------------------')
    print(f'NUMERO DE OPERACIONES DE {pacientes[id_mos][1]}: {conteo_operaciones}')
    print('----------------------------------------------------------------')
    archivo_aportacion = open(f'APORTACION_{id_mos}.txt','r')
    for R in archivo_aportacion:
        j = R
        t = j.replace("\n","")
        print(f'TOTAL DE APOPRTACION DEL PACIENTE A CONSULTORIO: ${t}')

def analisi_monetario():
    Gas = open('GASTOS.txt','r')
    Ing = open('INGRESOS.txt','r')
    gastos_engeneral = open('Gastos_Insumos.txt','r')
    gasto_tot = 0
    gasto_insumos=0
    ingre = 0
    for g in Gas:
        gasto_insumos = float(g)
    for i in Ing:
        ingre = float(i)
    for gg in gastos_engeneral:
        gasto_tot = float(gg)

    print('------------------GASTO ACUMULADO (insumos comprados hasta el momento)-------------')
    print(f'                           USTED HA GASTADO: ${gasto_tot}\n')
    print('------------------GASTO INSUMOS USADOS (insumos usados en todas las operaciones)-------------')
    print(f'                           USTED HA GASTADO: ${gasto_insumos}\n')
    print('------------------INGRESOS ACUMULADOS (ingresos por mano de obra de todas las operaciones)-------------')
    print(f'                           USTED HA GANADO: ${ingre}\n')
    print(f'SUS GANACIAS RESPECTO A INGRESOS E INSUMOS USADOS ES DE:  {ingre-gasto_insumos}')
    print(f'SUS GANACIAS RESPECTO A INGRESOS E INSUMOS COMPRADOS ES DE:  {ingre-gasto_tot}')
def menu():
    cont=True
    while cont:
        clear_console()
        print("1-Alta paciente")
        print("2-Habilitar paciente")
        print("3-Deshabilitar paciente")
        print("4-Ver expediente clínico")
        print("5-Reabastecer insumo")
        print("6-Ingresar insumo nuevo")
        print("7-Deshabilitar insumo")
        print("8-Habilitar insumo")
        print("9-Ver insumos")
        print("10-Alta operación")
        print("11-Ver operaciones por paciente")
        print("12-Ver historial de operaciones")
        print('13.- PANEL DE ANALÍTICAS')
        print("14-Cerrar programa")
        
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
            alta_insumo()
            input("OPRIMA ENTER PARA SALIR AL MENU")
            
        if opcion == 6:
            clear_console()
            habilitar_insumo()
            input("OPRIMA ENTER PARA SALIR AL MENU")
            
        if opcion == 7: 
            clear_console()
            inactivar()
            input("OPRIMA ENTER PARA SALIR AL MENU")
            
        if opcion == 8: 
            clear_console()
            activar()
            input("OPRIMA ENTER PARA SALIR AL MENU")
            
        if opcion == 9: 
            clear_console()
            ver_insumos()
            input("OPRIMA ENTER PARA SALIR AL MENU")
            
        if opcion == 10: 
            clear_console()
            alta_operacion()
            input("OPRIMA ENTER PARA SALIR AL MENU")
            
        if opcion == 11: 
            clear_console()
            ver_hist_pacientes()
            input("OPRIMA ENTER PARA SALIR AL MENU")

        if opcion == 12: 
            clear_console()
            ver_historial_operaciones()
            input("OPRIMA ENTER PARA SALIR AL MENU")
            
        if opcion == 13: 
            x = True
            while x:
                clear_console()
                print("1-Operaciones por Paciente Individualmente")
                print("2-Análisis de Ganancias")
                print("3.-Salir a menú principal")
                opci = int(input("OPCION ELEGIDA:  "))
                if opci == 1: 
                    clear_console()
                    operaciones_paciente()
                    input("OPRIMA ENTER PARA SALIR AL MENU")
                if opci == 2: 
                    clear_console()
                    analisi_monetario()
                    input("OPRIMA ENTER PARA SALIR AL MENU")
                elif opci == 3:
                    x = False
            input("OPRIMA ENTER PARA SALIR AL MENU")
            
        if opcion == 14: 
            cont=False
            input("OPRIMA ENTER PARA SALIR")


#----------------------------------------------------------------------
historiales = open('Hist_Oper.txt','a')
historiales.close
gastos_engeneral = open('Gastos_Insumos.txt','a')
gastos_engeneral.close
ingresos = open('INGRESOS.txt','a')
ingresos.close
ingresos = open('GASTOS.txt','a')
ingresos.close
idOperGen = open('NUMERO_OPERACIONES.txt', 'a')
idOperGenu = open('NUMERO_OPERACIONES_USUARIO.txt', 'a')
idOperGen.close
idOperGenu.close

listatamaño = open('tamalista.txt', 'a')
listatamaño.close
listatamaños = open('tamalista.txt', 'r')
g = 0
for e in listatamaños:
    if e != '':
        tamaño = int(e)
        g = tamaño - len(insumos)
if g != 0:
    for raw in range (0,g):
        insumos.append('')    
insunuevos = open("insumosNuevos.txt",'a')
insunuevos.close
idPacientesGeneral = open('ID_PACIENTES.txt', 'a')
idPacientesGeneral.close
leer_pacientes()
lectura_operaciones()
leer_insumos_predert()
menu()
