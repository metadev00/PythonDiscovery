#!/usr/bin/env python
import sys

lista_argumentos = sys.argv[1::]

if not lista_argumentos:
    print("none")
else:
    for palabra in lista_argumentos:
        if "ism" not in palabra:
            print(palabra + "ism")

