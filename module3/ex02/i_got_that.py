#!/usr/bin/env python 

finish_value = "STOP"

mensaje = input("What you gotta say? : ")

while True:         
	input_value = input("I got that! Anything else? :")
	if input_value  in (finish_value):
		print(f"I got that! Anything else? : {input_value.upper()}")
		break
