"""Modulo de Tarea: Punto de venta de flores"""

print("""Bienvendo al punto de venta de flores
Selecciones una opcion:
1- Agregar Rosas
2- Agregar Hortensias
3- Agregar Lirios
d- Descuento
8- Facturar
S- Salir\n""")


def rosa(rosas):
    """Funcion para ingresa rosas"""
    rosas = input("Ingrese cantidad de Rosas: ")
    global trosa
    # precio de rosas = 10
    trosa = int(rosas) * 10
    return trosa


def hort(hortensias):
    """Funcion para ingresa hortensias"""
    hortensias = input("Ingrese cantidad de Hortensias: ")
    global thort
    # precio de hortensias = 5
    thort = int(hortensias) * 5
    return thort


def liri(lirios):
    """Funcion para ingresa lirios"""
    lirios = input("Ingrese cantidad de Lirios: ")
    global tliri
    # precio de lirios = 7
    tliri = int(lirios) * 7
    return tliri


def desc(descuento):
    """Funcion para ingresa descuento"""
    descuento = input("Ingrese porcentaje de descuento: ")
    global pdesc
    pdesc = float((float(descuento))/100)
    return pdesc


def cobrar(tot):
    """Funcion para calcular y emitir total a cobrar"""
    global trosa
    global thort
    global tliri
    global pdesc
    stot = float(trosa + thort + tliri)
    tot = stot - (stot * pdesc)
    print('\nDesglose de Productos a Pagar\nTotal de Rosas: ', trosa,
          '\nTotal de Hortensias: ', thort,
          '\nTotal de Lirios: ', tliri,
          '\nPorcentaje de descuento: ', round((pdesc * 100), 3),
          '\nTotal a Pagar: ', tot)


option = str("")
pdesc = float(0)

while option != str.lower("s"):
    option = input(str("Ingrese opción: "))
    if option == str("1"):
        rosa(0)
    elif option == str("2"):
        hort(0)
    elif option == str("3"):
        liri(0)
    elif option == str.lower("d"):
        desc(0)
    elif option == str(8):
        cobrar(0)
    else:
        print("Opcion no válida o de salida")
