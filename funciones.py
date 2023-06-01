
#0
def stark_normalizar_datos(lista_p:list)->list:
    """Esta funcion normaliza datos del archivo data stark para poder
    exportarlos en otras funciones, copia la lista para que los
    valores originales no sean modificados

    Args:
        lista_p (list): lista del archivo data.stark pasada a parametro

    Returns:
        list: lista copiada
    """
    lista_copiada=list()
    if(len(lista_p)>0):
        for item in lista_p:
            if item["altura"] != float(item["altura"]):
                item["altura"] = float(item["altura"])

            if  item["peso"] != float(item["peso"]):
                item["peso"] = float(item["peso"])
        
            if item["fuerza"]!=int(item["fuerza"]):
                item["fuerza"]=int(item["fuerza"])            
            lista_copiada.append(item.copy())

        print("Datos normalizados")
        return lista_copiada
    else:
        print("“Error: Lista de héroes vacía”")
#1 , 1.1,1.2,1.3
def obtener_nombre(dicc_nombre:dict)->str:
    """funcion que recibe por parametro un diccionario que 
    representa un heroe , devuelve un string

    Args:
        dicc_nombre (dict): diccionario
    Returns:
        str: retorna nombre formateado
    """
    dato=(f"Nombre : {dicc_nombre['nombre']}")
    return dato
def imprimir_dato(palabra:str)->None:
    """recibe por parámetro un string y lo imprime en la consola. 

    Args:
        palabra (str): string
    """
    print(palabra)
def stark_imprimir_nombres_heroes(lista_heroes:list):
    """Funcion que recibe por parametro la lista de heroes e imprime
    por consola utilizando las funciones de los puntos anteriores.

    Args:
        lista_heroes (list): lista de heroes

    Returns:
        _type_: returna -1 si la lista esta vacia
    """
    if len(lista_heroes)>0:
        for nombre in lista_heroes:
            palabra=obtener_nombre(nombre)
            imprimir_dato(palabra)
    else:
        return -1
#2
def obtener_nombre_y_dato(dicc:dict,key:str)->str:
    """Funcion que recibe por parametro un diccionario y una key
    la cual representa el dato a obtener

    Args:
        dicc (dict): pisicion en la lista
        key (str): altura | fuerza | peso |  
    Return : retorna el string concatenado
    """
    dato = (f"Nombre : {dicc['nombre']:19s} | {key} : {dicc[key]}")
    return dato
#3
def stark_imprimir_nombres_alturas(lista_heroes:list)->None:
    """Funcion que recibe por parametro la lista de heroes copiada, itera e imprime
    nombres y algutas usando.Utiliza la funcion del punto 2 para imprimir los nombres

    Args:
        lista_heroes (list): lista de heroes 

    Returns:
        _type_: retorna -1 si la lista esta vacia
    """
    if len(lista_heroes)>0:
        for item in lista_heroes:
            obtener_nombre_y_dato(item,"altura")
    else:
        return -1
#4 4.1,4.2,4.3,4.4
def calcular_max(lista_heroes:list , key:str)->None:
    """Funcion que recibe por parametro la lista de heroes , una key la que 
    representa el dato que va hacer evaluado para determinar el maximo de la lista

    Args:
        lista_heroes (list): lista heroes
        key (str): altura | fuerza | peso |  
    """
    comparador=lista_heroes[0]
    for item in lista_heroes:
        if(comparador[key] < item[key]):
            comparador=item
    print(f"El mayor de tipo {key} :{comparador['nombre']}")
    return comparador
def calcular_min(lista_heroes:list , key:str)->str:
    """Funcion que recibe por parametro la lista de heroes , una key la que 
    representa el dato que va hacer evaluado para determinar el minimo de la lista

    Args:
        lista_heroes (list): lista heroes
        key (str):altura | fuerza | peso |  
    """
    comparador=lista_heroes[0]
    for item in lista_heroes:
        if(comparador[key] > item[key]):
            comparador=item
    print(f"El menor de tipo {key} :{comparador['nombre']}")
    return comparador
def calcular_max_min_dato(lista_heroes:list , estado:str , key:str)->str:
    """Funcion que recibe 3 valores por parametro , lista heroes, el estado
    (si saca max o min) y la key que seria el dato a comparar

    Args:
        lista_heroes (list): lista heroes
        estado (str):  maximo | minimo
        key (str): altura | fuerza | peso |  

    Returns:
        str: retorna el string concatenado 
    """
    if estado == "minimo":
        dato=calcular_min(lista_heroes,key)
    elif estado =="maximo":
        dato=calcular_max(lista_heroes,key)
    return dato
def stark_calcular_imprimir_heroe(lista_heroes:list , estado:str , key :str)->None:
    """Funcion que recibe 3 parametros ,la lista de heroes , estado que sera maximo o minimo 
    y la key para saber que se calculara.

    Args:
        lista_heroes (list): lista de heroes
        estado (str): maximo | minimo
        key (str): altura | fuerza | peso | 

    Returns:
        _type_: retorna -1 si no encuentra nada o imprime un mensaje
    """
    if (len(lista_heroes)>0):
        dato=calcular_max_min_dato(lista_heroes,estado,key)
        nombre=obtener_nombre_y_dato(dato,key)
        imprimir_dato(nombre)
    else:
        return -1
#5 5,1,5.2,5.3,5.4
def sumar_dato_heroe(lista_heroes:list,key:str)->str:
    """Funcion que recibe como parametro la lista de heroes y un string que
    reprenta dato/key de los heroes que se requiere sumar.

    Args:
        lista_heroes (list): lista de heroes
        key (str): altura | fuerza | peso |  

    Returns:
        str: retorna la suma o un mensaje que el diccionario esta vacio
    """
    sumatoria=0
    for item in lista_heroes:
        if(len(item) > 0):
            sumatoria+=item[key]
        else:
            print("diccionario vacio")
    return sumatoria      
def dividir(dividendo:int , divisor:int)->float:
    """funcion que recibe divivendo y divisor 

    Args:
        dividendo (int): dividendo
        divisor (int): divisor

    Returns:
        float: resutado de la division
    """
    if (divisor != 0):
        resultado=dividendo / divisor  
        return resultado
    else:
        return 0
def calcular_promedio(lista_heroes:list , key:str)->None:
    """Funcion que recibe por parametro la lista de heroes y una key para los calculos

    Args:
        lista_heroes (list): lista_Heroes
        key (str): altura | fuerza | peso | 

    Returns:
        _type_: retorna -1 o imprime un mensaje
    """
    promedio=sumar_dato_heroe(lista_heroes , key)
    total=dividir(promedio,len(lista_heroes))
    return total
def stark_calcular_imprimir_promedio_altura(lista_heroes:list):
    if len(lista_heroes) > 0:
        promedio=calcular_promedio(lista_heroes,"altura")
        imprimir_dato(promedio)
    else:
        return -1
#6 6.1 ,6.2
def imprimir_menu()->None:
    stark_marvel_app()
def validar_entero(numero:str)->bool:
    if numero.isdigit():
        return True
    else:
        return False
#7
def stark_marvel_app():
    print(f"""
    0-Normalizar datos
    1.1-Obtener nombre
    1.2-Imprimir dato
    1.3-Imprimir nombres heroes
    2-Obtener nombre y dato
    3-Imprimir nombres alturas
    4.1-Calcular maximo
    4.2-Calcular minimo
    4.3-Calcular maximo-minimo
    4.4-Stark imprimir heroe
    5.1-Sumar dato heroe
    5.2-Dividir
    5.3-Calcular promedio
    5.4-Stark imprimir promedio altura
    6.1-Imprimir menu
    6.2-Validar entero
    7-Stark marvel app 
    8-salir
    """)
    opcion = input("    Ingresar opcion >: ")
    return opcion 