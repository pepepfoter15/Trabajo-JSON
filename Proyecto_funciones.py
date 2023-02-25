#Archivo con la funciones del proyecto de JSON

def menu():
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

def listar_informacion():
    print("Listar todos los id y nombres (con apellidos) de los ganadores de estos premios.")

def contar_informacion():
    print("Indica cuantas veces aparece las categorías química y paz.")

def buscar_filtar_informacion():
    print("Filtrar pidiendo el año y la categoría y que muestre todas las caracterías de los galardonados o premiados (laureates).")

def buscar_informacion_relacionada():
    print("Pedir el id del autor y que nos muestre todo sobre ese id, el año y la categoría (su nombre, su motivo (motivation) y la parte de ese mismo (share)).")

def intercambiar_autor():
    print("Pidiendo el id de la persona que quieres cambiar y el id del que quieres remplazar, intercambiar el nombre y el apellido de ellos.")
