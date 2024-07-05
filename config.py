from random import randint
import libreria as l
import csv
def menu():
    print("1) Registrar los consumos: ")
    print("2) Listar todos los consumos: ")
    print("3) Imprimir una hoja de consumo: ")
    print("4) Buscar un consumo por ID: ")
    print("5) Salir del programa: ")
    return input("Escoja una opción: ")
def validarnum(opc):
    if opc>"0" and opc.isnumeric():
        return True
    else:
        return False
def validartext(opc):
    if opc.replace(" ","").isalpha()==True:
        return True
    else:
        return False
def registrarconsumo(nombre,edad,equipo,consumoviernes,consumosabado,consumodomingo):
    jugador={}
    id=randint(10000,100000)
    jugador['id']=id
    jugador['nombre']=nombre
    jugador['edad']=edad
    if equipo=="1":
        jugador['equipo']=l.equipos[0]
    elif equipo=="2":
        jugador['equipo']=l.equipos[1]
    elif equipo=="3":
        jugador['equipo']=l.equipos[2]
    elif equipo=="4":
        jugador['equipo']=l.equipos[3]
    elif equipo=="5":
        jugador['equipo']=l.equipos[4]
    consumototal=int(consumoviernes)+int(consumosabado)+int(consumodomingo)
    if consumototal>=3:
        jugador['consumoviernes']=consumoviernes
        jugador['consumosabado']=consumosabado
        jugador['consumodomingo']=consumodomingo
        l.jugadores.append(jugador)
        return l.jugadores
    else:
        return False
def validarnumcafe(opc):
    if opc>="0" and opc.isnumeric():
        return True
    else:
        return False
def listarconsumo():
    for consumos in l.jugadores:
        print(f"ID Consumo: {consumos['id']}")
        print(f"Nombre: {consumos['nombre']}")
        print(f"Edad: {consumos['edad']}")
        if consumos['equipo']=="genios_garrafa":
            print(f"Equipo: Los genios de la garrafa")
        elif consumos['equipo']=="compiladores_despiertos":
            print(f"Equipo: Los compiladores despiertos")
        elif consumos['equipo']=="codigo_borracho":
            print(f"Equipo: Código Borracho")
        elif consumos['equipo']=="programadores_perezosos":
            print(f"Equipo: Los programadores perezosos")
        elif consumos['equipo']=="ctrl_alt_derrota":
            print(f"Equipo: Ctrl+Alt+Derrota")
        print(f"Viernes: {consumos['consumoviernes']}")
        print(f"Sábado: {consumos['consumosabado']}")
        print(f"Domingo: {consumos['consumodomingo']}")

def consumoporid(id):
    for consumos in l.jugadores:
        if consumos['id']==int(id):
            print(f"ID Consumo: {consumos['id']}")
            print(f"Nombre: {consumos['nombre']}")
            print(f"Edad: {consumos['edad']}")
            if consumos['equipo']=="genios_garrafa":
                print(f"Equipo: Los genios de la garrafa")
            elif consumos['equipo']=="compiladores_despiertos":
                print(f"Equipo: Los compiladores despiertos")
            elif consumos['equipo']=="codigo_borracho":
                print(f"Equipo: Código Borracho")
            elif consumos['equipo']=="programadores_perezosos":
                print(f"Equipo: Los programadores perezosos")
            elif consumos['equipo']=="ctrl_alt_derrota":
                print(f"Equipo: Ctrl+Alt+Derrota")
            print(f"Viernes: {consumos['consumoviernes']}")
            print(f"Sábado: {consumos['consumosabado']}")
            print(f"Domingo: {consumos['consumodomingo']}")
            break

def idexiste(id):
    for consumos in l.jugadores:
        if consumos['id']==int(id):
            return True
        else:
            return False
def menuequipo():
    print("1)Los genios de la garrafa")
    print("2)Los compiladores despiertos")
    print("3)Código borracho")
    print("4)Programadores perezosos")
    print("5)Ctrl+alt+derrota")
    return input("Seleccione una opción para mostrar: ")
def imprimirhoja(equipo):
    if equipo=="1":
        equipo=="genios_garrafa"
    elif equipo=="2":
        equipo=="compiladores_despiertos"
    elif equipo=="3":
        equipo=="codigoborracho"
    elif equipo=="4":
        equipo=="programadores_perezosos"
    elif equipo=="5":
        equipo=="ctrl_alt_derrota"
        for consumos in l.jugadores:
            if consumos['equipo']==equipo:
                with open('equipo.csv','w',newline="",encoding="utf8") as archivo:
                    campos=['id','nombre','edad','equipo','consumoviernes','consumosabado','consumodomingo']
                    escritor=csv.DictWriter(archivo,fieldnames=campos)
                    escritor.writeheader()
                    escritor.writerows(consumos)
def existeequipo(equipo):
    print (equipo)
    variable="asd"
    if equipo=="1":
        variable=="genios_garrafa"
    elif equipo=="2":
        variable=="compiladores_despiertos"
    elif equipo=="3":
        variable=="codigoborracho"
    elif equipo=="4":
        variable=="programadores_perezosos"
    elif equipo=="5":
        variable=="ctrl_alt_derrota"
    else:
        "No existe"
    print("asd")
    print(variable)
    if equipo:
        for consumos in l.jugadores:
            if consumos['equipo']==variable:
                return True
            else:
                return False


        
