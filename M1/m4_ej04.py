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

if cant_puntos == 3:
    print("Contiene 3 puntos")

elif cant_puntos < 3:
    print("Error tiene menos puntos que la cantidad requerida")
else:
    print("Error tiene mas puntos que la cantidad requerida")

for i in "0123456789":
    conteo = ip.count(i)
    if conteo > 0:
        print(f"Se encontro {conteo} '{i}' en la IP.")

    




