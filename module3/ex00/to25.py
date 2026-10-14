#!/usr/bin/env python 

input_value = int( input("Enter a number less than 25\r\n"))
	
iterar = 25
i = input_value

if input_value >= iterar:
	print("Error")
else:
	while  i <=  iterar:
	       print(f"Inside the loop, my variable is {i}")
	       i+=1

