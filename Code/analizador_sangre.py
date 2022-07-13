"""
Ejercicio nivel 2: Analizador de examen sanguíneo
Modulo de calculos.

Temas:f
* Variables.
* Tipos de datos.
* Expresiones aritmeticas.
* Instrucciones basicas y consola.
* Dividir y conquistar: funciones y paso de parametros.
* Especificacion y documentacion.
* Instrucciones condicionales.
* Diccionarios.
@author: Cupi2
NOTA IMPORTANTE PARA TENER EN CUENTA EN TODAS LAS FUNCIONES DE ESTE MODULO:

"""
#infectados={}

"""examenes={"e1": {'id': 0, 'genero': 'M', 'edad': 0, 'PPM': 0, 'Hb': 0, 'CGB': 0, 'glicemia': 260, 'LDL': 0,
            'HDL': 0, 'trigliceridos': 0, 'CT': 245, 'CL': 0, 'CP': 0, 'tiempo': 0, 'GCH': 0}, "e2": {'id': 1,
            'genero': 'M', 'edad': 1, 'PPM': 1, 'Hb': 1, 'CGB': 1, 'glicemia': 84, 'LDL': 1, 'HDL': 1, 'trigliceridos': 1,
            'CT': 1, 'CL': 1, 'CP': 1, 'tiempo': 1, 'GCH': 1}, "e3": {'id': 2, 'genero': 'M', 'edad': 2,
            'PPM': 2, 'Hb': 2, 'CGB': 2, 'glicemia': 2, 'LDL': 2, 'HDL': 2, 'trigliceridos': 2, 'CT': 2, 'CL': 2, 'CP': 2,
            'tiempo': 2, 'GCH': 2}, "e4": {'id': 3, 'genero': 'F', 'edad': 0, 'PPM': 3, 'Hb': 100, 'CGB': 3,
            'glicemia': 3, 'LDL': 3, 'HDL': 3, 'trigliceridos': 3, 'CT': 3, 'CL': 3, 'CP': 3, 'tiempo': 3, 'GCH': 9.1}}
"""

def crear_paciente(id:int, genero:str, edad:int, PPM:int,
                   Hb:int, CGB:float, glicemia:int, LDL:float, HDL:float, trigliceridos:float, CT:float,
                   CL:float, CP:float, tiempo:int, GCH:int) -> dict:
    """Crear un diccionario que representa un paciente que se realizo examen de sangre con todos sus atributos inicializados.
    :param id: Id del paciente y de su muestra sanguínea
    :param genero: Género del paciente que se realizó el examen de sangre
    :param edad: Edad del paciente que se realizó el examen de sangre
    :param PPM: Pulsaciones por minuto del paciente al momento de la toma de la muestra
    :param Hb: Hemoglobina en la muestra de sangre (g/L)
    :param CGB: Conteo de glóbulos blancos en la muestra de sangre (x10^3/uL)
    :param glicemia: glicemia en ayunas detectada en la muestra de sangre (mg/dl)
    :param LDL: Lipoproteínas de baja densidad en la muestra de sangre (mg/dl)
    :param HDL: Lipoproteínas de alta densidad en la muestra de sangre (mg/dl)
    :param trigliceridos: Trigliceridos en la muestra de sangre (mg/dl)
    :param CT: Colesterol total en la muestra de sangre (mg/dl)
    :param CL: Conteo de linfocitos en la muestra sangre (10^3/uL)
    :param CP: Conteo de plaquetas en la muestra de sangre (10^3/uL)
    :param tiempo: Tiempo de procesamiento de la muestra de sangre (min)
    :param GCH: Gonadotropina coriónica humana en la muestra de sangre (mIU/ml)
    :return:
        dict: Diccionario con los resultados del exámen sanguíneo
    """

    #TODO: completar y remplazar la siguiente linea por el resultado correcto

    paciente = {"id": id, "genero": genero, "edad": edad, "PPM": PPM,
                "Hb": Hb, "CGB": CGB, "glicemia": glicemia, "LDL": LDL, "HDL": HDL, "trigliceridos": trigliceridos,
                "CT": CT, "CL": CL, "CP": CP, "tiempo": tiempo, "GCH": GCH}

    return paciente

def buscar_examen(id:int, e1:dict,e2:dict, e3:dict, e4:dict)->dict:
    """
    Busca en cuál de los 4 diccionarios que se pasan por parámetro está el examen de sagnre
    cuyo id es dado por parametro.
    Si no se encuentra el exámen, se retorna None.
    :param id: El id del exámen de sangre que se desea buscar
    :param e1: Diccionario con la información del exámen de sangre 1
    :param e2: Diccionario con la información del examén de sangre 2
    :param e3: Diccionario con la información del examén de sangre 3
    :param e4: Diccionario con la información del examén de sangre 4
    :return:
        dict: Diccionario del exámen de sangre cuyo id fue dado por parámetro. Retorna None si no lo encuentra
    """
    # TODO: completar y remplazar la siguiente linea por el resultado correcto
    diccionario = None
    
    if id == e1["id"]:
        diccionario = e1
    elif id == e2["id"]:
        diccionario = e2
    elif id == e3["id"]:
        diccionario = e3
    elif id == e4["id"]:
        diccionario =e4
    

    return diccionario


# Especificar genero
def confirmar_embarazo(examen:dict)->bool:
    """
    Valida si hay embarazo dependiendo de los niveles de la GCH en el examen de sangre con
    id dado por parámetro
    :param examen: Diccionario con el examen de sangre a analizar
    :return:
        bool: True si el examen de sangre confirma el embarazo, False de lo contrario
    """
    # TODO: completar y remplazar la siguiente linea por el resultado correcto

    #genero = str(examen["genero"])
    #niveles = int(examen["GCH"])

    if examen["genero"] == "M":
        respuesta = "El examen registrado es de una persona de genero masculino."

    else:
        if examen["GCH"] < 9:
            respuesta = False

        else:
            respuesta = True

    return respuesta


def validar_pulsaciones(examen:dict)->str:
    """
    Valida si el paciente tiene taquicardía, bradicardía o normalidad .
    :param examen: Diccionaro con el examen sanguíneo al cual se le verificará las pulsaciones por minuto (PPM)
    :return:
        str: retorna taquicardia si las PPM están por encima de los límites normales, retorna bradicardia si están
        por debajo de los límites normales y retorna normalidad en cualquier otro caso:
    """
    # TODO: completar y remplazar la siguiente linea por el resultado correcto
    
    genero = examen["genero"]
    pulsaciones = examen["PPM"]
    edad = examen["edad"]
    x = "Las caracteristicas de la persona no estan clasificadas."

    if genero == "M":

        if edad > 19 and edad < 30:
            if pulsaciones > 85:
                respuesta = "Taquicardia."
            if pulsaciones > 61 and pulsaciones < 85:
                respuesta = "Normalidad."
            if pulsaciones < 61:
                respuesta = "Bradicardia."
        else:
            respuesta = x

        if edad > 29 and edad < 40:
            if pulsaciones > 85:
                respuesta = "Taquicardia."
            if pulsaciones > 63 and pulsaciones < 85:
                respuesta = "Normalidad."
            if pulsaciones < 63:
                respuesta = "Bradicardia."
        else:
            respuesta = x

        if edad > 39 and edad < 50:
            if pulsaciones > 89:
                respuesta = "Taquicardia."
            if pulsaciones > 65 and pulsaciones < 89:
                respuesta = "Normalidad."
            if pulsaciones < 65:
                respuesta = "Bradicardia."
        else:
            respuesta = x

        if edad > 50:
            if pulsaciones > 90:
                respuesta = "Taquicardia."
            if pulsaciones > 67 and pulsaciones < 89:
                respuesta = "Normalidad."
            if pulsaciones < 67:
                respuesta = "Bradicardia."
        else:
            respuesta = x

    else:
        respuesta = "Las caracteristicas de la persona no estan clasificadas."

    if genero == "F":
        if edad > 19 and edad < 30:
            if pulsaciones > 96:
                respuesta = "Taquicardia."
            if pulsaciones > 71 and pulsaciones < 95:
                respuesta = "Normalidad."
            if pulsaciones < 71:
                respuesta = "Bradicardia."
        else:
            respuesta = x

        if edad > 29 and edad < 40:
            if pulsaciones > 98:
                respuesta = "Taquicardia."
            if pulsaciones > 71 and pulsaciones < 97:
                respuesta = "Normalidad."
            if pulsaciones < 71:
                respuesta = "Bradicardia."
        else:
            respuesta = x

        if edad > 39 and edad < 50:
            if pulsaciones > 100:
                respuesta = "Taquicardia."
            if pulsaciones > 73 and pulsaciones < 90:
                respuesta = "Normalidad."
            if pulsaciones < 73:
                respuesta = "Bradicardia."
        else:
            respuesta = x

        if edad > 50:
            if pulsaciones > 104:
                respuesta = "Taquicardia."
            if pulsaciones > 75 and pulsaciones < 103:
                respuesta = "Normalidad."
            if pulsaciones < 75:
                respuesta = "Bradicardia."
        else:
            respuesta = x

    else:
        respuesta = x

    return respuesta


def confirmar_anemia(examen:dict) -> bool:
    """
    Valida si el examen de sangre muestra anémia en la sangre dada la hemoglobina en sangre
    :param examen: Diccionario con el examen de sangre al cual se le verificará anemia
    :return:
        bool: True si hay evidencia de anemia, False de lo contrario
    """
    # TODO: completar y remplazar la siguiente linea por el resultado correcto
    
    genero = examen["genero"]
    edad = examen["edad"]
    hb = examen["Hb"]
    hto = round(3.1 * hb)
    embarazo = confirmar_embarazo(examen)
    respuesta = "Las caracteristicas de la persona no estan clasificadas."

    if edad < 5 and hto < 33:
        respuesta = "Anemia."
    else:
        respuesta = "Sin anemia."

    if edad > 4 and edad < 12 and hto < 34:
        respuesta = "Anemia."
    else:
        respuesta = "Sin anemia."

    if edad > 11 and edad < 15 and hto < 36:
        respuesta = "Anemia."
    else:
        respuesta = "Sin anemia."

    if genero == "F" and embarazo == False and edad > 11 and edad < 15 and hto < 36:
        respuesta = "Anemia."
    else:
        respuesta = "Sin anemia."

    if genero == "F" and embarazo == True and hto < 33:
        respuesta = "Anemia."
    else:
        respuesta = "Sin anemia."

    if genero == "M" and edad > 15 and hto < 39:
        respuesta = "Anemia."
    else:
        respuesta = "Sin anemia."

    return respuesta

def contar_hipoglicemicos(e1:dict,e2:dict, e3:dict, e4:dict)->int:
    """
    Cuanto cuantos pacientes son hipoglicémicos
    :param e1: Diccionario con la información del exámen de sangre 1
    :param e2: Diccionario con la información del examén de sangre 2
    :param e3: Diccionario con la información del examén de sangre 3
    :param e4: Diccionario con la información del examén de sangre 4
    :return:
        int: Número de pacientes que son hipoglicémicos
    """
    # TODO: completar y remplazar la siguiente linea por el resultado correcto

    contador = 0
    e1 = e1["glicemia"]
    e2 = e2["glicemia"]
    e3 = e3["glicemia"]
    e4 = e4["glicemia"]

    if e1 < 70:
        contador += 1

    if e2 < 70:
        contador += 1

    if e3 < 70:
        contador += 1

    if e4 < 70:
        contador += 1

    return contador

def validar_infecciones(e1:dict,e2:dict, e3:dict, e4:dict)-> str:
    """
    Valida cuales exámenes de sangre presentan posiblidad de infecciones dependiendo del conteo de globulos
    blancos (CGB)
    :param e1: Diccionario con la información del exámen de sangre 1
    :param e2: Diccionario con la información del examén de sangre 2
    :param e3: Diccionario con la información del examén de sangre 3
    :param e4: Diccionario con la información del examén de sangre 4
    :return:
        str: una cadena con todos los id's de los exámenes de sangre que presentan posibilidad de infección
        separados por comas
    """
    # TODO: completar y remplazar la siguiente linea por el resultado correcto

    e1 = e1["CGB"]
    e2 = e2["CGB"]
    e3 = e3["CGB"]
    e4 = e4["CGB"]
    x = ""
    if e1 > 11000:
        x += str(e1["id"]) + ","

    if e2 > 11000:
        x += str(e2["id"]) + ","

    if e3 > 11000:
        x += str(e3["id"]) + ","

    if e4 > 11000:
        x += str(e4["id"]) + ","
    

    return str(x)

def calcular_promedio(e1:dict,e2:dict, e3:dict, e4:dict)->float:
    """
    Calcula el tiempo promedio de procesamiento para las muestras de sangre
    :param e1: Diccionario con la información del exámen de sangre 1
    :param e2: Diccionario con la información del examén de sangre 2
    :param e3: Diccionario con la información del examén de sangre 3
    :param e4: Diccionario con la información del examén de sangre 4
    :return:
        float: Tiempo promedio de procesamiento de las muestras de sangre en minutos.
    """
    
    # TODO: completar y remplazar la siguiente linea por el resultado correcto
    e1 = e1["tiempo"]
    e2 = e2["tiempo"]
    e3 = e3["tiempo"]
    e4 = e4["tiempo"]

    promedio = round((e1 + e2 + e3 + e4) / 4)

    return promedio

# Entra el diccionario, tipo y objetivo
def actualizar_glicemia(tipo:int, objetivo:int, examen:dict)-> int:
    """
    Dado el id de un examen de sangre, calcular el número de unidades de insulina, del tipo especificado,
    necesarias para corregir los niveles de azúcar en sangre hasta el nivel objetivo dado por parámetro.
    Se debe actualizar el valor de la glicemia en el examen de sangre especificado, añadir la llave
    de unidades_Suministradas con el valor de las unidades de insulina para corregir el azúcar en sangre
    :param examen: Diccionario con el examen de sangre al cual se le corregirá la glicemia en sangre
    :param tipo: Tipo de insulina que difiere en la concentracion de insulina en la ampolla para la correción.
                De este depende el factor de correción.
    :param objetivo: Nivel de azúcar en sangre objetivo
    :return:
        int: Número de unidades de insulina del tipo especificado para realizar la corrección. Si no se necesita
        ninguna unidad, retorna 0.
    """
    # TODO: completar y remplazar la siguiente linea por el resultado correcto

    
    glicemia_act = examen["glicemia"]

    if glicemia_act < 250:
        return str("El paciente no se encuentra en estado critico.")

    else:

        if tipo == 1:
            factor = 40
        else:
            factor = 50

        resultado = float((glicemia_act - objetivo) / factor)

        examen["glicemia"] = objetivo

    return round(resultado)

def validar_diabetes(examen:dict)->str:
    """
    Valida si el examen de sangre muestra indices de diabetes de acuerdo a la glicemia en ayunas
    :param examen: Diccionario con el examen de sangre a validar
    :return:
        str: Rertorna diabetes o prediabetes si la glicemia lo soporta, de lo contrario retorna normalidad
    """
    
    # TODO: completar y remplazar la siguiente linea por el resultado correcto

    
    glicemia = examen["glicemia"]

    if glicemia > 125:
        respuesta = "diabetes."

    if glicemia > 109 and glicemia < 126:
        respuesta = "prediabetes."

    if glicemia < 125:
        respuesta = "niveles normales."

    return respuesta

def calcular_riesgo_cardiaco(examen:dict)->int:
    """
    Calular los puntos de riesgo cardíaco a partir del perfil lipídico
    :param examen: Examen de sangre al cual se le calcularan los puntos de riesgo
    :return:
        int: puntos de riesgo cardiaco del examen dado por parámetro. Si hay dos o más pacientes con el mismo 
        nivel de riesgo retorna el primero.
    """

    # TODO: completar y remplazar la siguiente linea por el resultado correcto

    
    colesterol = examen["CT"]
    diabetes = validar_diabetes(examen)
    ldl = examen["LDL"]
    genero = examen["genero"]
    hdl = examen["HDL"]
    trigliceridos = examen["trigliceridos"]
    contador = 0

    if colesterol > 239:
        contador += 1

    if diabetes == "Diabetes." and ldl > 100:
        contador += 1

    if diabetes != "Diabetes." and ldl > 130:
        contador += 1

    if genero == "M" and hdl < 40:
        contador += 1

    if genero == "F" and hdl < 50:
        contador += 1

    if trigliceridos > 149:
        contador += 2
    examen["riesgo"] = contador

    return contador

def evaluar_prioridad(e1:dict,e2:dict, e3:dict, e4:dict)->dict:
    """
    Retorna el diccionario con el examen de sangre del paciente que tiene mayor prioridad para ser atendido
    dado los puntos de riesgo cardiaco del perfíl lipídico.
    :param e1: Diccionario con la información del exámen de sangre 1
    :param e2: Diccionario con la información del examén de sangre 2
    :param e3: Diccionario con la información del examén de sangre 3
    :param e4: Diccionario con la información del examén de sangre 4
    :return:
        retorna el diccionario con el paciente prioriatrio dado sus puntos de riesgo cardiaco.
    """
    
    # TODO: completar y remplazar la siguiente linea por el resultado correcto

    #riesgo_e1 = calcular_riesgo_cardiaco(0)
    #riesgo_e2 = calcular_riesgo_cardiaco(1)
    #riesgo_e3 = calcular_riesgo_cardiaco(2)
    #riesgo_e4 = calcular_riesgo_cardiaco(3)

    #maximo = max(riesgo_e1, riesgo_e2, riesgo_e3, riesgo_e4)

    def C_riesgo(examen)->None:
        colesterol = examen["CT"]
        diabetes = validar_diabetes(examen)
        ldl = examen["LDL"]
        genero = examen["genero"]
        hdl = examen["HDL"]
        trigliceridos = examen["trigliceridos"]
        contador = 0

        if colesterol > 239:
            contador += 1

        if diabetes == "Diabetes." and ldl > 100:
            contador += 1

        if diabetes != "Diabetes." and ldl > 130:
            contador += 1

        if genero == "M" and hdl < 40:
            contador += 1

        if genero == "F" and hdl < 50:
            contador += 1

        if trigliceridos > 149:
            contador += 2
        examen["riesgo"] = contador

    C_riesgo(e1)
    C_riesgo(e2)
    C_riesgo(e3)
    C_riesgo(e4)

    prioridad = max(e1["riesgo"],e2["riesgo"],e3["riesgo"],e4["riesgo"])

    if prioridad == e1["riesgo"]:
        paciente = e1

    elif prioridad == e2["riesgo"]:
        paciente = e2

    elif prioridad == e3["riesgo"]:
        paciente = e3

    elif prioridad == e4["riesgo"]:
        paciente = e4

    return paciente

def validar_CLL(examen:dict, frotis:bool) -> int:
    """
    Valida si el paciente debe ser diagnosticado con CLL dado su conteo de linfocitos, plaquetas y si el resultado del
    examen de frotis.
    :param examen: Diccionario con el examen de sangre a validar
    :param frotis: Resultado del examen del frotis de las células sanguíneas.
    :return:
        int: Retorna 0 si es negativo para CLL, retorna 1 si es positivo para CLL y retorna -1 si se debe realizar
        una biopsia de médula osea para confirmar el diagnóstico.
    """
    
    # TODO: completar y remplazar la siguiente linea por el resultado correcto

    
    cl = examen["CL"]
    cp = examen["CP"]

    if cl >= 10:
        respuesta = 1

    elif cl >= 8 and cl <= 9.999 and cp < 145.000:
        respuesta = 1

    elif cl < 8 and frotis == True:
        respuesta = -1

    else:
        respuesta = 0

    return respuesta



