#Archivo con la funciones del proyecto de JSON.
import json
import os
import math

with open('Proyecto JSON.json') as r:
    premiosnobeles = json.load(r)

def menu(opcion):
    opcion=int(input('''
         PROYECTO JSON
    -----------------------------------------------
    1. Listar información
    2. Contar información
    3. Buscar o filtar información
    4. Buscar informacion relacionada
    5. Intercambiar autor
    6. Salir
    -----------------------------------------------
    Introduce una opción de este menú ->'''))
    return(opcion)

def listar_informacion(premionobeles):
    print("Listar todos los id y nombres (con apellidos) de los ganadores de estos premios.")
    for premiados in premionobeles["prizes"]:
        for id_nombres in premiados["laureates"]:
                print("El id es ",id_nombres["id"]," y el nombre es ",id_nombres["firstname"])


def contar_informacion(premionobeles):
    print("Indica cuantas veces aparece las categorías química y paz.")
    contador_chemistry = 0
    contador_peace = 0
    for premiados in premionobeles["prizes"]:
        if premiados["category"] == "chemistry":
            contador_chemistry = contador_chemistry + 1
        elif premiados["category"] == "peace":
            contador_peace = contador_peace + 1

    print("Hay ",contador_chemistry,"premios de química.")
    print("Hay ",contador_peace,"premios de paz.")




def buscar_filtar_informacion():
    print("Filtrar pidiendo el año y la categoría y que muestre todas las caracterías de los galardonados o premiados (laureates).")

def buscar_informacion_relacionada():
    print("Pedir el id del autor y que nos muestre todo sobre ese id, el año y la categoría (su nombre, su motivo (motivation) y la parte de ese mismo (share)).")

def intercambiar_autor():
    print("Pidiendo el id de la persona que quieres cambiar y el id del que quieres remplazar, intercambiar el nombre y el apellido de ellos.")
