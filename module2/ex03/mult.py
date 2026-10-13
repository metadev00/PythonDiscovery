#!/usr/bin/env python 


frst_number = int(input("Enter the first number:\r\n"))
sec_number = int(input("Enter the second number:\r\n"))

mult =  frst_number * sec_number

print(f'{frst_number} x {sec_number} = {mult}')

if mult > 0 :
	print("The result is positive.")
elif mult < 0:
	print("The result is negative.")
else:
    print("The result is positive and negative.")

