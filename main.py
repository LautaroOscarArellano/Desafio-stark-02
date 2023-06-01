from data_stark  import lista_personajes
from funciones import*
import os

while True:
    os.system("cls")
    match(stark_marvel_app()):
        case "0":
            datos_normalizados=stark_normalizar_datos(lista_personajes) # check  
        case "1.1":
                nombre=obtener_nombre(datos_normalizados[4])
                print(nombre)
        case "1.2":
            dato=input("Ingresar palabra : ")
            imprimir_dato(dato)
        case "1.3":
            stark_imprimir_nombres_heroes(datos_normalizados)
        case "2":
            a=obtener_nombre_y_dato(datos_normalizados[0],"fuerza")
        case "3":
            stark_imprimir_nombres_alturas(datos_normalizados)
        case "4.1":
            b=calcular_max(datos_normalizados , "fuerza")
        case "4.2":
            c=calcular_min(datos_normalizados , "fuerza")
        case "4.3":
            heroe=calcular_max_min_dato(datos_normalizados,"maximo","altura")
        case "4.4":
            stark_calcular_imprimir_heroe(datos_normalizados,"maximo","altura")
        case "5.1":
            d=sumar_dato_heroe(datos_normalizados,"fuerza")
            print(d)
        case "5.2":
            dividendo=int(input("Dividendo : "))
            divisor=int(input("Divisor : "))
            e=dividir(dividendo,divisor)
            print("Resultado" , e)
        case "5.3":
            f=calcular_promedio(datos_normalizados,"fuerza")
            print(f"{f:.2f}")#guardar
        case "5.4":
            g=stark_calcular_imprimir_promedio_altura(datos_normalizados)
        case "6.1":
            imprimir_menu()
        case "6.2":
            numero=input("Ingresar numeros :")
            h=validar_entero(numero)
            print(h)
        case "7":
            stark_marvel_app()
        case _:
            print("Opcion incorrecta")
    os.system("pause")   




