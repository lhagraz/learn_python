# **Ejercicio 4 — Validador básico de IP**
'''El usuario ingresa una dirección IP como string. 
Verifica e imprime si el string contiene exactamente 3 puntos 
(condición necesaria pero no suficiente para ser una IPv4 válida).
 Muestra también la longitud del string y cuántas veces aparece cada 
 número del 0 al 9 en la dirección. No uses expresiones regulares.
'''
ip = input("Ingrese dirección IP: ")

cant_puntos = ip.count(".")

longitud = len(ip)

print("\n" + "=" * 45)
print("          VALIDADOR DE DIRECCIÓN IPv4")
print("=" * 45)
print(f"   IP analizada : {ip}")
print(f"   Longitud     : {longitud} caracteres")
print(f"   Puntos       : {cant_puntos}")
print("=" * 45)
#Validacion cantidad de punto
if cant_puntos == 3:
    print("   [VÁLIDO]  Contiene exactamente 3 puntos")
elif cant_puntos < 3:
    print(f"  [ERROR]   Faltan {3 - cant_puntos} punto(s)")
else:
    print(f"  [ERROR]   Sobran {cant_puntos - 3} punto(s)")
#frecuencia de los digitos de la IP.
print("=" * 45)
print("  Frecuencia de dígitos:")
print()

for i in "0123456789":
    conteo = ip.count(i)
    if conteo > 0:
        print(f"    Dígito '{i}' → {conteo} vez/veces")


print("\n" + "=" * 45)

    




