#!/usr/bin/env python
import sys

if len(sys.argv) > 1:

	argumento = sys.argv[1]
	input_value = input("What was the parameter? ")

	if argumento != input_value:
		print("Nope, sorry...")
	else:
		print("Good job!")

else:
	print("none")
