from data_stark  import lista_personajes
from funciones import*
import os

flag_normalizado=False
while True:
    os.system("cls")
    match(stark_marvel_app()):
        case "0":
            datos_normalizados=stark_normalizar_datos(lista_personajes) # check  
            flag_normalizado=True
        case "1.1":
                if flag_normalizado:
                    nombre=obtener_nombre(datos_normalizados[4])
                    print(nombre)
                else:
                    print("Funcion 0 primero")
        case "1.2":
            dato=input("Ingresar palabra : ")
            imprimir_dato(dato)
        case "1.3":
            if flag_normalizado:
                stark_imprimir_nombres_heroes(datos_normalizados)
            else:
                print("Funcion 0 primero")
        case "2":
            if flag_normalizado:
                a=obtener_nombre_y_dato(datos_normalizados[0],"fuerza")
            else:
                print("Funcion 0 primero")
        case "3":
            if flag_normalizado:
                stark_imprimir_nombres_alturas(datos_normalizados)
            else:
                print("Funcion 0 primero")
        case "4.1":
            if flag_normalizado:
                b=calcular_max(datos_normalizados , "fuerza")
            else:
                print("Funcion 0 primero")
        case "4.2":
            if flag_normalizado:
                c=calcular_min(datos_normalizados , "fuerza")
            else:
                print("Funcion 0 primero")
        case "4.3":
            if flag_normalizado:
                heroe=calcular_max_min_dato(datos_normalizados,"maximo","altura")
            else:
                print("Funcion 0 primero")
        case "4.4":
            if flag_normalizado:
                stark_calcular_imprimir_heroe(datos_normalizados,"maximo","altura")
            else:
                print("Funcion 0 primero")
        case "5.1": 
            if flag_normalizado:
                d=sumar_dato_heroe(datos_normalizados,"fuerza")
                print(d)
            else:
                print("Funcion 0 primero")
        case "5.2":
            while True:
                try:
                    dividendo=int(input("Dividendo : "))
                    break
                except ValueError:
                    print("ingresaste vacio ")
            while True:
                try:
                    divisor=int(input("Divisor : "))
                    break
                except ValueError:
                    print("ingresaste vacio ")    
            e=dividir(dividendo,divisor)
            print("Resultado" , e)
        case "5.3":
            if flag_normalizado:
                f=calcular_promedio(datos_normalizados,"fuerza")
                print(f"{f:.2f}")#guardar
            else:
                print("Funcion 0 primero")
        case "5.4":
            if flag_normalizado:
                g=stark_calcular_imprimir_promedio_altura(datos_normalizados)
            else:
                print("Funcion 0 primero")
        case "6.1":
            imprimir_menu()
        case "6.2":
            numero=input("Ingresar numeros :")
            h=validar_entero(numero)
            print(h)
        case "7":
            stark_marvel_app()
        case "8":
            break
        case _:
            print("Opcion incorrecta")
    os.system("pause")   




