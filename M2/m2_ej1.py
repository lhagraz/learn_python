#**Ejercicio 1 — Clasificador de puertos con if/elif**
'''Reescribe el ejercicio 9 del Módulo 1 usando `if/elif/else` en lugar de lógica booleana. 
El resultado debe ser idéntico, pero el código debe ser más claro y legible. Incluye
los mismos 4 rangos y la validación de negativos.'''
nro_port = int(input("Ingrese numero de puerto: "))


#Verificación de puerto
if 0 <= nro_port <= 1023 :
    mensaje = "Puerto bien conocido (sistema)"

elif 1024 <= nro_port <= 49151:
    mensaje = "Puerto registrado (aplicación)"

elif 49152 <= nro_port <= 65535:
    mensaje = "Puerto dinámico/privado"

else:
    mensaje = "Puerto inválido"
    

print("\n" + "=" * 45)
print("            CLASIFICADOR DE PUERTO")
print("=" * 45)
print(f"  Número de puerto : {nro_port} ")
print(f"  Estado de puerto : {mensaje} ")
print("=" * 45)