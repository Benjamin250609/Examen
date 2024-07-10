import Funciones as fn

datos = {}

while True:
    print("----------Bienvenido---------------")
    print("1- Asignar sueldos")
    print("2- Clasificar sueldos")
    print("3- Ver estadisticas")
    print("4- Reporte de sueldos")
    print("5- Salir del programa")


    opcion = input("Ingrese la opcion deseada: ")

    if opcion == "1":
        datos = fn.asignar_sueldo()
    elif opcion == "2":
        fn.clasificar_sueldos(datos)
    elif opcion == "3":
        fn.ver_estadisticas(datos)
    elif opcion == "4":
        fn.reporte_sueldo(datos)
    elif opcion == "5":
        print("Finalizando Programa....")
        print("Desarrollado por Benjamin Perez")
        print("RUT 21.464.072-4")
        break
    else:
        print("Ingrese una opcion valida (1-5)")
    



