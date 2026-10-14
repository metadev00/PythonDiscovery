numeros = [2, 8, 9, 48, 8, 22, -12, 2]

#Opciones:
#print(numeros)
'''
print("[",end=" ")
for value in numeros:
    print(value,end=" ")
print("]",end=" ")
'''
print("[ " + " ".join(map(str, numeros)) + " ]")