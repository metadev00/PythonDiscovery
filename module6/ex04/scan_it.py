#!/usr/bin/env python
import sys
import re

array = sys.argv

if (len(array) <= 2 ):
	print("none")
else:
		param  = array[1]
		text = array[2]
		matches = len(re.findall(param,text))
		
		if matches > 1:
			print(matches)
		else:
			print("none")		
