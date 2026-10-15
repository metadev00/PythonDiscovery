
#!/usr/bin/env python3
import sys

lista_argumentos = sys.argv[1:]
array_list = []

# Comprobar que hay exactamente 2 parámetros
if len(lista_argumentos) != 2:
    print("none")
else:
    primero = int(lista_argumentos[0])
    segundo = int(lista_argumentos[1])

    # El primero debe ser estrictamente menor
    if primero < segundo:
        for i in range(primero, segundo + 1):
            array_list.append(i)

        print(array_list)
    else:
        print("none")
