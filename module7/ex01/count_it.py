#!/usr/bin/env python 
import sys

array_parametros = sys.argv
if len(array_parametros) > 1:
	print(f"parameters: {len(array_parametros) - 1}")

	for i in array_parametros[1::]:
		print(f"{i}: {len(i)}")
else:
	print("none")
