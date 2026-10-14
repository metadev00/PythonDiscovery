#!/usr/bin/env python 

iter_horizontal = 0
iter_vertical = 0 
val_max = 10 # Num max

#Iteracion vertical
while iter_vertical <= val_max:
	#Iteracion horizonatl
	print(f"Table of {iter_vertical} : ", end=" ")
	while iter_horizontal <= 10:
		print(f"{iter_horizontal * iter_vertical}", end =" ")
		iter_horizontal+=1
	
	iter_horizontal = 0
	iter_vertical += 1
	
	print("")
