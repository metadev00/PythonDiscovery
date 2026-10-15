#!/usr/bin/env python

import sys

parametros = sys.argv

txt_zeta = ""

if len(parametros) > 1:
	txt_parametros = parametros[1] 
	num_zeta_aparecido =int( txt_parametros.count('z'))
	if  num_zeta_aparecido == 0:
		print("none")
	else:
		for _ in range num_zeta_aparecido:
			txt_zeta+=z
		print(txt_zeta)
		
else:
	print("none")	
