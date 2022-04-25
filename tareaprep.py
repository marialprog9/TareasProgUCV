
print("Ayudemos al caracol a salir del hoyo, en el dia el caracol sube Ld (m) pero en la noche al quedarse dormido resbala y desciende Ln (m), cuantos diras tardara en salir?:")

Ld = float(input("Digite un valor de Ld (m):"))
Ln = float(input("Digite un valor de Ln (m):"))
H = float(input("Indique altura del hoyo (m):"))

operacion = H/(Ld - Ln)

if(Ld-Ln)>0:
    print(f"\nEl caracol saldra del hoyo en: {operacion} dias")

else:
    print("El caracol no puede salir")
