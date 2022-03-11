print (" Calculadora con condicional")
operacion = ""

while operacion != "salida":
    numero1 = float(input("Digite un numero:"))
numero2 = float (input("Digite un numero:"))
operacion = input ("Digite la operacion: ")

if operacion == 's':
    suma = numero1+numero2
    print(f"\nLa suma es: {suma}")

elif operacion == 'R':
    resta= numero1-numero2
    print(f"\nLa resta es: {resta}")

print ("Fin del programa")

    
