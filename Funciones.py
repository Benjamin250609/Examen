import csv, random

trabajadores = ["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]

def asignar_sueldo():
    sueldos ={}
    for trabajador in trabajadores:
        sueldo = random.randint(300000,2500000)
        Descuento_Salud = (sueldo*0.07)
        Descuento_AFP = (sueldo*0.12)
        sueldoLiquido = sueldo - Descuento_Salud - Descuento_AFP
        sueldos[trabajador] = {"Sueldo Base": sueldo,
                               "Descuento Salud": Descuento_Salud,
                               "Descuento AFP": Descuento_AFP,
                               "Sueldo Liquido": sueldoLiquido}
    print("Sueldos asignados exitosamente :) ")
    print("")
    return sueldos

def clasificar_sueldos(datos):
    print("")
    if datos == {}:
        print("Asigne primero los sueldos con la opcion 1 :)")
        print("")
        return
    menores = {}
    intermedio = {}
    mayor = {}
    sueldos = []
    for empleado,dinero in datos.items():
        ganancia = dinero["Sueldo Base"]
        sueldos.append(ganancia)
    for nombre,claves in datos.items():
        if claves["Sueldo Base"] < 800000:
            menores[nombre] = claves["Sueldo Base"]
        elif claves["Sueldo Base"] >= 800000 and claves["Sueldo Base"] <=2000000:
            intermedio[nombre] = claves["Sueldo Base"]
        else:
            mayor[nombre] = claves["Sueldo Base"]
    print("Sueldos menores a $800.000, en total:",len(menores))
    print(f"Nombre Empleado\t\t Sueldo")
    for nombre_trabajador,sueldo in menores.items():
        print(f"{nombre_trabajador}\t\t ${sueldo}")
    print("Sueldos entre $800.000 y $2.000.000, en total:",len(intermedio))
    print(f"Nombre Empleado\t\t Sueldo")
    for nombre_trabajador,sueldo in intermedio.items():
        print(f"{nombre_trabajador}\t\t ${sueldo}")
    print("Sueldos mayores a $2.000.000, en total:",len(mayor))
    print(f"Nombre Empleado\t\t Sueldo")
    for nombre_trabajador,sueldo in mayor.items():
        print(f"{nombre_trabajador}\t\t ${sueldo}")
    print("Total Sueldos $",sum(sueldos))
    print("")

def ver_estadisticas(datos):
    print("")
    if datos == {}:
        print("Asigne primero los sueldos con la opcion 1 :)")
        print("")
        return
    sueldos = []
    for empleado,dinero in datos.items():
        ganancia = dinero["Sueldo Base"]
        sueldos.append(ganancia)
    sueldo_maximo = max(sueldos)
    sueldo_minimo = min(sueldos)
    promedio = round(sum(sueldos)/len(sueldos))
    multiplicador = 1
    for multiplicar in sueldos:
        multiplicador = multiplicador * multiplicar
    media_geometrica = round(multiplicador**(1/len(sueldos)))
    for nombre,sueldo in datos.items():
        if sueldo["Sueldo Base"] == sueldo_maximo:
            print(f"El sueldo maximo es de ${sueldo_maximo} de la persona {nombre}")
        if sueldo["Sueldo Base"] == sueldo_minimo:
            print(f"El sueldo minimo es de ${sueldo_minimo} de la persona {nombre}")
    print("El promedio de sueldos es de: $",promedio)
    print("La media geometrica es de: $",media_geometrica)
    print("")

def reporte_sueldo(datos):
    print("")
    if datos == {}:
        print("Asigne primero los sueldos con la opcion 1 :)")
        print("")
        return
    with open("ReporteSueldos.csv","w",newline="") as archivo:
        escritor = csv.writer(archivo,delimiter=",")
        escritor.writerow(["Nombre empleado","Sueldo Base","Descuento Salud","Descuento AFP","Sueldo Liquido"])
        for nombre,claves in datos.items():
            escritor.writerow([nombre,claves["Sueldo Base"],round(claves["Descuento Salud"]),round(claves["Descuento AFP"]),round(claves["Sueldo Liquido"])])
    print(f"Nombre empleado\t Sueldo Base\t Descuento Salud\t Descuento AFP\t Sueldo Liquido")
    for nombre,claves in datos.items():
        print(f"{nombre}\t ${claves["Sueldo Base"]}\t ${round(claves["Descuento Salud"])}  \t\t${round(claves["Descuento AFP"])}  \t\t${round(claves["Sueldo Liquido"])}")
    print("")
    print("Archivo crado con exito")
    print("")


