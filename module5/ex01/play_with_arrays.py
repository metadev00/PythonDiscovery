numeros = [2, 8, 9, 48, 8, 22, -12, 2]
print("Original array [ " + " ".join(map(str, numeros)) + " ]")


#Opcion 1

print("New arra: [",end=" ")
for i in numeros:
    print(i + 2,end=" ")

print("]",end=" ")


#Opcion 1
''' 
new_array = map(lambda x: x + 2, numeros)
print("New arra: [ " + " ".join(map(str, new_array)) + " ]")
'''

