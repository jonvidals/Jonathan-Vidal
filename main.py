import config as c
import libreria as l
while True:
    opc=c.menu()
    validarmenu=c.validarnum(opc)
    if opc=="1" and validarmenu==True:
        while True:
            nombre=input("Ingrese su nombre: ")
            validartext=c.validartext(nombre)
            if validartext==True:
                print(f"Nombre ingresado: {nombre}")
                break
            else:
                print("Cáracter no válido")
        while True:
            edad=input("Ingrese su edad: ")
            validarnum=c.validarnum(edad)
            if validarnum==True:
                print(f"Edad ingresada: {edad}")
                break
            else:
                print("Cáracter no válido")
        while True:
            equipo=input("Ingrese al equipo que pertenece(Ingrese un número): \n1)Los genios de la Garrafa\n2)Los compiladores despiertos\n3)Código borracho\n4)Los programadores perezosos\n5)Ctrl+Alt+Derrota")
            validarnum=c.validarnum(equipo)
            if validartext==True and equipo=="1":
                print(f"Equipo ingresado: Los genios de la garrafa: {equipo}")
                break
            elif validartext==True and equipo=="2":
                print(f"Equipo ingresado: Los compiladores despiertos: {equipo}")
                break
            elif validartext==True and equipo=="3":
                print(f"Equipo ingresado: Código borracho: {equipo}")
                break
            elif validartext==True and equipo=="4":
                print(f"Equipo ingresado: Los programadores perezosos: {equipo}")
                break
            elif validartext==True and equipo=="5":
                print(f"Equipo ingresado: Ctrl+Alt+Derrota{equipo}")
                break            
            else:
                print("Cáracter no válido")
        while True:
            cafeviernes=input("Ingrese cantidad de cafés del día viernes: ")
            validarnum=c.validarnumcafe(cafeviernes)
            if validarnum==True:
                print(f"Cafes día viernes: {cafeviernes}")
                break
            else:
                print("Cáracter no válido")
        while True:
            cafesabado=input("Ingrese cantidad de cafés del día sábado: ")
            validarnum=c.validarnumcafe(cafesabado)
            if validarnum==True:
                print(f"Cafes día sábado: {cafesabado}")
                break
            else:
                print("Cáracter no válido")
        while True:
            cafedomingo=input("Ingrese cantidad de cafés del día domingo: ")
            validarnum=c.validarnumcafe(cafedomingo)
            if validarnum==True:
                print(f"Cafes día domingo: {cafedomingo}")
                break
            else:
                print("Cáracter no válido")
        agregarcafe=c.registrarconsumo(nombre,edad,equipo,cafeviernes,cafesabado,cafedomingo)
        if agregarcafe!=False:
            print(agregarcafe)
        else:
            print("No cumple con el total de requísito de 3 cafés en los 3 días.")
    if opc=="2" and validarmenu==True:
        if l.jugadores:
            c.listarconsumo()
        else:
            print("No hay jugadores para mostrar")
    if opc=="3" and validarmenu==True:
        while True:
            equipo=c.menuequipo()
            validaropc=c.validarnum(equipo)
            if validaropc==True:
                break
            else:
                print("Cáracter inválido")
        existeequipo=c.existeequipo(equipo)
        if existeequipo==True:
            c.imprimirhoja(equipo)
        else:
            print(equipo)
            print("No existe ese equipo")
    if opc=="4" and validarmenu==True:
        if l.jugadores:
            while True:
                id=input("Ingrese su ID: ")
                validarnum=c.validarnum(id)
                if validarnum==True:
                    break
                else:
                    print("Cáracter inválido")
            existe=c.idexiste(id)
            if existe==True:
                c.consumoporid(id)
            else:
                print("ID no encontrado")              
        else:
            print("No hay nada para mostrar")
    if opc=="5" and validarmenu==True:
        print("fin del programa")
        break