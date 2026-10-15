#!/usr/bin/env python
import sys

array = sys.argv[1::]


if len(array) > 2 :
	reversed_numbers = array[::-1]
	for i in reversed_numbers:
		print(f"{i}")
		
else:
	print("none")
