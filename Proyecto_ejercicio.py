#EJERCICIO PROYECTO JSON
from Proyecto_funciones import *
import json

opcionelegida=0

while opcionelegida != 6:
    opcionelegida=menu(opcionelegida)
    if opcionelegida == 1:
        opción1 =listar_informacion(premiosnobeles)
    elif opcionelegida == 2:
        opción2=contar_informacion(premiosnobeles)
    elif opcionelegida == 3:
        opción3 =buscar_filtar_informacion(premiosnobeles)
    elif opcionelegida == 4:
        opción4 =buscar_informacion_relacionada(premiosnobeles)
    elif opcionelegida == 5:
        opción5 =intercambiar_autor(premiosnobeles)

if opcionelegida == 6:
    print("Usted ha salido del programa.")
