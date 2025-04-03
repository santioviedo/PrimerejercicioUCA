    #pedir al usuario 2 valores lo tienen que invertir que el valor A tome el valor B  y el B tome el valor de A

A = input("Ingrese el valor de A: ")
B = input("Ingrese el valor de B: ")

A, B = B, A

print("Después del intercambio:")
print("A =", A)
print("B =", B)
