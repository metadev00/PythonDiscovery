#!/usr/bin/env python
import sys

datos_parametro = sys.argv
len_args = len(sys.argv)

if len_args > 1 : 
	print(f"Number of parameters: {len(sys.argv)-1}.") 
else:
	print("Number of parameters: 0.")
