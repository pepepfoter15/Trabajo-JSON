#EJERCICIO PROYECTO JSON
from Proyecto_funciones import *

with open('Proyecto JSON.json', 'r') as f:
    lista_enbruto = f.readlines()

lista=[]


opcionelegida=0

while opcionelegida != 6:
    opcionelegida=menu()
    if opcionelegida == 1:
        opción1 =listar_informacion(lista)
    elif opcionelegida == 2:
        opción2=contar_informacion(lista)
    elif opcionelegida == 3:
        opción3 =buscar_filtar_informacion(lista)
    elif opcionelegida == 4:
        opción4 =buscar_informacion_relacionada(lista)
    elif opcionelegida == 5:
        opción5 =intercambiar_autor(lista)

if opcionelegida == 6:
    print("Usted ha salido del programa.")
