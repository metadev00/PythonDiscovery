#!/usr/bin/env python

array_original = [2, 8, 9, 48, 8, 22, -12, 2]
array_modificado = []

print(array_original)

for i in array_original:
    if i > 5:
    	array_modificado.append(i+2)

unique_items_modificado = set(array_modificado)


print(unique_items_modificado)
