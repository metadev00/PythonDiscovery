#!/usr/bin/env python
import sys

array = sys.argv

if len(array) > 1 :
	print(array[1].upper())
else:
	print("none")
