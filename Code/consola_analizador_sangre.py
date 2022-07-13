"""
Ejercicio nivel 2: Analizador de examen sanguíneo.
Modulo de interaccion por consola.

Temas:
* Variables.
* Tipos de datos.
* Expresiones aritmeticas.
* Instrucciones basicas y consola.
* Dividir y conquistar: funciones y paso de parametros.
* Especificacion y documentacion.
* Instrucciones condicionales.
* Diccionarios.
@author: Cupi2
"""

import analizador_sangre as mod


def mostrar_paciente(examen: dict) -> None:
    """ Muestra en pantalla los resultados de un examen de sangre de un paciente.
    Parametros:
        examen (dict): El examen de sangre del que se van a mostrar los detalles.
    """
    id = examen["id"]
    genero = examen["genero"]
    edad = examen["edad"]
    PPM = examen["PPM"]
    Hb = examen["Hb"]
    CGB = examen["CGB"]
    glicemia = examen["glicemia"]
    LDL = examen["LDL"]
    HDL = examen["HDL"]
    trigliceridos = examen["trigliceridos"]
    CT = examen["CT"]
    CL = examen["CL"]
    CP = examen["CP"]
    tiempo = examen["tiempo"]
    GCH = examen["GCH"]

    print("ID: " + str(id) + " - Género: " + str(genero) + " - Edad: " + str(edad) +
          "\nPPM: " + str(PPM) + " - Hb: " + str(Hb) + " - CGB: " + str(CGB) + " - Glicemia: " + str(glicemia) +
          "\nLDL: " + str(LDL) + " - HDL: " + str(HDL) + "Triglicéridos: " + str(trigliceridos) + " - CT: " + str(CT) +
          "\nCL: " + str(CL) + " - CP: " + str(CP) + " Tiempo: " + str(tiempo) + "GCH: " + str(GCH))


def ejecutar_confirmar_embarazo(e1: dict, e2: dict, e3: dict, e4: dict) -> None:
    """
    Ejecuta la función que valida si hay embarazo dependiendo de los niveles de la GCH en el examen de sangre con
    id dado por parámetro
     Parámetros:
        e1 (dict): Diccionario con la información del exámen 1.
        e2 (dict): Diccionario con la información del exámen 2.
        e3 (dict): Diccionario con la información del exámen 3.
        e4 (dict): Diccionario con la información del exámen 4.
    El programa debe mostrar al usuario: "Los resultados del exámen sugieren que la paciente está embarazada." si el 
    exámen lo confirma. De lo contrario, se espera que el mensaje sea: "Los resultados del exámen sugieren que la paciente NO está embarazada."
    """
    id = int(input("Ingrese el identificador de la paciente que quiere buscar"))
    #TODO: Completar
    x = mod.buscar_examen(id, e1, e2, e3, e4)
    respuesta = (mod.confirmar_embarazo(x))
    if respuesta == True:
        print("Los resultados del exámen sugieren que la paciente está embarazada.")
    elif respuesta == False:
        print("Los resultados del exámen sugieren que la paciente no está embarazada.")
    else:
        print(respuesta)

def ejecutar_validar_pulsaciones(e1: dict, e2: dict, e3: dict, e4: dict) -> None:
    """
    Ejecuta la función que valida si el paciente tiene taquicardía, bradicardía o normalidad .
    Parámetros:
        e1 (dict): Diccionario con la información del exámen 1.
        e2 (dict): Diccionario con la información del exámen 2.
        e3 (dict): Diccionario con la información del exámen 3.
        e4 (dict): Diccionario con la información del exámen 4.
        Si la respuesta es normalidad, el programa debe mostrar el string: El paciente no presenta ninguna anormalidad en su pulso.
        De lo contrario, debe mostrar el string: El paciente presenta YYYY. Donde YYYY puede ser taquicardia o bradicardia
    """
    id = int(input("Ingrese el identificador del paciente que quiere buscar"))
    x = mod.buscar_examen(id, e1, e2, e3, e4)
    respuesta = mod.validar_pulsaciones(x)
    print("El paciente presenta " + str(respuesta))
    


def ejecutar_confirmar_anemia(e1: dict, e2: dict, e3: dict, e4: dict) -> None:
    """
    Ejecuta la función que valida si el examen de sangre muestra anémia en la sangre dada la hemoglobina en sangre
    Parámetros:
        e1 (dict): Diccionario con la información del exámen 1.
        e2 (dict): Diccionario con la información del exámen 2.
        e3 (dict): Diccionario con la información del exámen 3.
        e4 (dict): Diccionario con la información del exámen 4.
        Si el resultado indica anemia,  el programa debe mostrar el string: El paciente presneta indicaciones de sufir anemia.
        De lo contrario, debe mostrar el string: El paciente NO presenta indicaciones de sufir anemia.
    """
    id = int(input("Ingrese el identificador del paciente que quiere buscar"))
    x = mod.buscar_examen(id, e1, e2, e3, e4)
    if x == "Anemia.":
        resultado = "El paciente presneta indicaciones de sufir anemia."
    else:
        resultado = "El paciente NO presenta indicaciones de sufir anemia."
    print(resultado)

def ejecutar_contar_hipoglicemicos(e1: dict, e2: dict, e3: dict, e4: dict) -> None:
    """
    Ejecuta la función que valida cuántos pacientes son hipoglicémicos
    Parámetros:
        e1 (dict): Diccionario con la información del exámen 1.
        e2 (dict): Diccionario con la información del exámen 2.
        e3 (dict): Diccionario con la información del exámen 3.
        e4 (dict): Diccionario con la información del exámen 4.
        El programa debe retornar el string: Hay X pacientes hipoglicémicos. Donde X es la cantidad 
        de pacientes hipoglicémicos en el hispital
    """
    print("Hay " + str(mod.contar_hipoglicemicos(e1, e2, e3, e4)) + " pacientes hipoglicémicos.")


def ejecutar_validar_infecciones(e1: dict, e2: dict, e3: dict, e4: dict) -> None:
    """
    Ejecuta la función que valida cuáles exámenes de sangre presentan posiblidad de infecciones dependiendo del conteo de globulos
    blancos (CGB)
    Parámetros:
        e1 (dict): Diccionario con la información del exámen 1.
        e2 (dict): Diccionario con la información del exámen 2.
        e3 (dict): Diccionario con la información del exámen 3.
        e4 (dict): Diccionario con la información del exámen 4.
        El programa debe retornar el string: Los siguientes pacientes presentan riesgo de tener infecciones: YYYY. 
        Donde YYYY es el listado de ids de los pacientes, separados por comas, que tienen indicios de infección.
    """
    if mod.validar_infecciones(e1, e2, e3, e4) == "":
        print("Los pacientes no presentan infecciones")
    else:
        print("Los siguientes pacientes presentan riesgo de tener infecciones " + str(mod.validar_infecciones(e1, e2, e3, e4)))

def ejecutar_calcular_promedio(e1: dict, e2: dict, e3: dict, e4: dict) -> None:
    """
    Ejecuta la función que calcula el tiempo promedio de procesamiento para las muestras de sangre
    Parámetros:
        e1 (dict): Diccionario con la información del exámen 1.
        e2 (dict): Diccionario con la información del exámen 2.
        e3 (dict): Diccionario con la información del exámen 3.
        e4 (dict): Diccionario con la información del exámen 4.
        El sistema debe mostrar le string:El tiempo promedio en que las muestras tardan en procesarse es X. 
        Donde X es el tiempo promedio de procesamiento de las muestras
    """
    print("El tiempo promedio en que las muestras tardan en procesarse es " + str(mod.calcular_promedio(e1, e2, e3, e4)) + " minutos")

def ejecutar_actualizar_glicemia(e1: dict, e2: dict, e3: dict, e4: dict) -> None:
    """
    Dado el id de un examen de sangre, calcular el número de unidades de insulina, del tipo especificado,
    necesarias para corregir los niveles de azúcar en sangre hasta el nivel objetivo dado por parámetro.
    Se debe actualizar el valor de la glicemia en el examen de sangre especificado, añadir la llave
    de unidades_Suministradas con el valor de las unidades de insulina para corregir el azúcar en sangre
    Parámetros:
        e1 (dict): Diccionario con la información del exámen 1.
        e2 (dict): Diccionario con la información del exámen 2.
        e3 (dict): Diccionario con la información del exámen 3.
        e4 (dict): Diccionario con la información del exámen 4.

    El programa debe mostrar el siguiente String: X unidades de insulina deben ser administradas al paciente.
    Donde X es el número de unidades que deben ser administradas para realizar la corrección. 
    """
    id = int(input("Ingrese el identificador del paciente que quiere buscar"))
    # TODO: Completar
    tipo = int(input("Tipo de apolleta a suministrar (1 o 2): "))
    objetivo = int(input("Valor al cual se necesita llegar: "))
    if tipo == 1 or tipo == 2:
        examen = mod.buscar_examen(id, e1, e2, e3, e4)
        x = str(mod.actualizar_glicemia(tipo, objetivo, examen))
        devolver = x + " unidades de insulina deben ser administradas al paciente."
    else:
        devolver = "El tipo de ampolleta no existe."
    
    print(devolver)


def ejecutar_validar_diabetes(e1: dict, e2: dict, e3: dict, e4: dict) -> None:
    """
    Ejecuta la función que valida si el examen de sangre muestra indices de diabetes de acuerdo a la glicemia en ayunas
    Parámetros:
        e1 (dict): Diccionario con la información del exámen 1.
        e2 (dict): Diccionario con la información del exámen 2.
        e3 (dict): Diccionario con la información del exámen 3.
        e4 (dict): Diccionario con la información del exámen 4.4
        Si el resultado es normalidad, se debe mostrar el mensaje:El paciente no presenta ninguna anormalidad.
        De lo contrario, debe mostrar un mensaje de la siguiente manera: El paciente presenta X. 
        Donde X puede ser diabetes o prediabetes dependiendo del caso. 
    """
    id = int(input("Ingrese el identificador del paciente que quiere buscar"))
    x = mod.buscar_examen(id, e1, e2, e3, e4)
    if mod.validar_diabetes(x) == "niveles normales.":
        print("El paciente no presenta ninguna anormalidad.")
    else:
        print("El paciente presenta " + str(mod.validar_diabetes(x)))

def ejecutar_evaluar_prioridad(e1: dict, e2: dict, e3: dict, e4: dict) -> dict:
    """
    Ejecuta la función que evalúa qué paciente tiene mayor prioridad para ser atendido
    dado los puntos de riesgo cardiaco del perfíl lipídico.
    Parámetros:
        e1 (dict): Diccionario con la información del exámen 1.
        e2 (dict): Diccionario con la información del exámen 2.
        e3 (dict): Diccionario con la información del exámen 3.
        e4 (dict): Diccionario con la información del exámen 4.
        El sistema mostrar el string: El paciente con ID X debe ser atendido con prioridad. 
        Donde X es el id del paciente con mayor prioridad en la escala de riesgo.
    """
    examen=mod.evaluar_prioridad(e1, e2, e3, e4)
    print("El paciente con ID " + str(examen["id"]) + " debe ser atendido con prioridad")


def ejecutar_validar_CLL(e1: dict, e2: dict, e3: dict, e4: dict) -> None:
    """
    Valida si el paciente debe ser diagnosticado con CLL dado su conteo de linfocitos, plaquetas y si el resultado del
    examen de frotis.
    :param examen: Diccionario con el examen de sangre a validar
    :param frotis: Resultado del examen del frotis de las células sanguíneas.
    Si el resultado es 1, el programa debe mostrar: Los resultados sugieren que el paciente es positivo para CLL
    Si el resultado es -1, el programa debe mostrar: Se debe realizar una biopsia de médula para confirmar el diagnóstico de CLL
    Si el resultado es 0, el programa debe mostrar: El paciente no presenta indicaciones de CLL
    """
    id = int(input("Ingrese el identificador del paciente que quiere buscar"))
    frotis = bool(
        int(input("Ingresa 1 si el examen de Frotis salió positivo, 0 de lo contrario")))
    
    examen = mod.buscar_examen(id, e1, e2, e3, e4)
    if mod.validar_CLL(examen, frotis) == -1:
        print("Se debe realizar una biopsia de médula para confirmar el diagnóstico de CLL")
    elif mod.validar_CLL(examen, frotis) == 0:
        print("El paciente no presenta indicaciones de CLL")
    elif mod.validar_CLL(examen, frotis) == 1:
        print("Los resultados sugieren que el paciente es positivo para CLL")
    


def iniciar_aplicacion():
    """Inicia la ejecucion de la aplicacion por consola.
    Esta funcion primero crea cuatro resultados de exámenes de sangre.
    Luego la funcion le muestra el menu al usuario y espera a que seleccione una opcion.
    Esta operacion se repite hasta que el usuario seleccione la opcion de salir.
    """
    examen1 = mod.crear_paciente(
        1, "M", 20, 88, 20, 11.5, 280, 89.7, 50, 120.8, 240, 7.9, 150, 25, 0)
    examen2 = mod.crear_paciente(
        2, "F", 30, 90, 9, 10.5, 69, 98.3, 60, 100.9, 225, 9.8, 141, 35, 10)
    examen3 = mod.crear_paciente(
        3, "F", 69, 70, 15, 12.5, 115, 138.6, 40, 150.3, 260, 8.2, 160, 15, 2)
    examen4 = mod.crear_paciente(
        4, "M", 33, 60, 10, 9.9, 65, 102.5, 55, 120.8, 236, 10.6, 167, 43, 0)

    ejecutando = True
    while ejecutando:
        print("\n\nResultado de los exámenes" + ("-"*50))
        print("Examen de Sangre 1")
        mostrar_paciente(examen1)
        print("-"*50)

        print("Examen de Sangre 2")
        mostrar_paciente(examen2)
        print("-"*50)

        print("Examen de Sangre 3")
        mostrar_paciente(examen3)
        print("-"*50)

        print("Examen de Sangre 4")
        mostrar_paciente(examen4)
        print("-"*50)

        ejecutando = mostrar_menu_aplicacion(
            examen1, examen2, examen3, examen4)

        if ejecutando:
            input("Presione cualquier tecla para continuar ... ")


def mostrar_menu_aplicacion(e1: dict, e2: dict, e3: dict, e4: dict) -> bool:
    """Le muestra al usuario las opciones de ejecucion disponibles.
    Parametros:
        e1 (dict): Diccionario que contiene la informacion del examen 1.
        e2 (dict): Diccionario que contiene la informacion del examen 2.
        e3 (dict): Diccionario que contiene la informacion del examen 3.
        e4 (dict): Diccionario que contiene la informacion del examen 4.
    Retorno:
        Esta funcion retorna True si el usuario selecciono una opcion diferente
        a la opcion que le permite salir de la aplicacion.
        Esta funcion retorna False si el usuario selecciono la opcion para salir
        de la aplicacion.

    """
    print("Menu de opciones")
    print(" 1 - Confirmar embarazo")
    print(" 2 - Validar PPM")
    print(" 3 - Confirmar Anémia")
    print(" 4 - Contar hipoglicémicos")
    print(" 5 - Validar infecciones")
    print(" 6 - Promedio de exámenes")
    print(" 7 - Actualizar Glicemia")
    print(" 8 - Validar diabetes")
    print(" 9 - Evaluar prioridad")
    print(" 10 - Validar CLL")
    print(" 11 - Salir de la aplicacion.")

    opcion_elegida = input("Ingrese la opcion que desea ejecutar: ").strip()

    continuar_ejecutando = True

    if opcion_elegida == "1":
        ejecutar_confirmar_embarazo(e1, e2, e3, e4)
    elif opcion_elegida == "2":
        ejecutar_validar_pulsaciones(e1, e2, e3, e4)
    elif opcion_elegida == "3":
        ejecutar_confirmar_anemia(e1, e2, e3, e4)
    elif opcion_elegida == "4":
        ejecutar_contar_hipoglicemicos(e1, e2, e3, e4)
    elif opcion_elegida == "5":
        ejecutar_validar_infecciones(e1, e2, e3, e4)
    elif opcion_elegida == "6":
        ejecutar_calcular_promedio(e1, e2, e3, e4)
    elif opcion_elegida == "7":
        ejecutar_actualizar_glicemia(e1, e2, e3, e4)
    elif opcion_elegida == "8":
        ejecutar_validar_diabetes(e1, e2, e3, e4)
    elif opcion_elegida == "9":
        ejecutar_evaluar_prioridad(e1, e2, e3, e4)
    elif opcion_elegida == "10":
        ejecutar_validar_CLL(e1, e2, e3, e4)
    elif opcion_elegida == "11":
        continuar_ejecutando = False
    else:
        print("La opcion " + opcion_elegida + " no es una opcion valida.")
    return continuar_ejecutando


iniciar_aplicacion()
