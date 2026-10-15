#!/usr/bin/env python

array_original = [2, 8, 9, 48, 8, 22, -12, 2]
array_modificado = []

print(f"Original array:  {array_original} ")


#Opcion 1


for i in array_original:
    if i > 5:
    	array_modificado.append(i+2)
     

print(f"New array: {array_modificado}")
