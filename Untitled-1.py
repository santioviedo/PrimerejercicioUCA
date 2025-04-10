contra = "UCA2025"
entrada = ""
intentos = 0 

while entrada != contra and intentos < 3:
    entrada = input("ingrese su contrasenia: ")
    if entrada != contra:
        print("la contrasenia es incorrecta ")
        intentos+1

if entrada == contra:
    print("has accedido")
else:
    print("no hay mas intentos ")
