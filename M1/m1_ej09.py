#**Ejercicio 9 — Clasificador de puertos**
'''El usuario ingresa un número de puerto. El programa debe clasificarlo e imprimir la categoría correcta:
- 0–1023 → "Puerto bien conocido (sistema)"
- 1024–49151 → "Puerto registrado (aplicación)"
- 49152–65535 → "Puerto dinámico/privado"
- Fuera de rango → "Puerto inválido"

Usa únicamente operadores de comparación y booleanos (aún no hemos visto `if`, así que construye 
la lógica con `and`, `or`, `print` y expresiones booleanas creativas — es un reto intencional).

'''
nro_port = int(input("Ingrese numero de puerto: "))


#Verificación de puerto
verificacion = (
(nro_port >= 0 and  nro_port <= 1023 and "Puerto bien conocido (sistema)") or
(nro_port > 1023 and  nro_port <= 49151 and "Puerto registrado (aplicación)") or
(nro_port > 49151 and  nro_port <= 65535 and "Puerto dinámico/privado") or
(nro_port < 0 and "Puerto inválido") or
(nro_port > 65535 and "Puerto inválido")
)
print("\n" + "=" * 45)
print("            CLASIFICADOR DE PUERTO")
print("=" * 45)
print(f"  Número de puerto : {nro_port} ")
print(f"  Estado de puerto : {verificacion} ")
print("=" * 45)