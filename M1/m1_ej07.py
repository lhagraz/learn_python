#**Ejercicio 7 — Calculadora de entropía básica**
'''La entropía de una contraseña depende del conjunto de 
caracteres usado y su longitud. Dado un set de caracteres posibles (input: número entero) 
y la longitud de la contraseña (input: entero), calcula el número total de combinaciones
 posibles con la fórmula `combinaciones = set_size ** length`. Muestra el resultado y evalúa 
 si supera 1 billón (`10 ** 12`) imprimiendo `True` o `False`.'''
set_size = int(input("Ingrese el tamaño del set de caracteres: "))
length = int(input("Ingrese la longitud de la contraseña: "))
combinaciones = set_size ** length

es_segura = combinaciones > 10 ** 12

print("\n" + "=" * 45)
print("       CALCULADORA DE ENTROPÍA")
print("=" * 45)
print(f"   Set de caracteres : {set_size}")
print(f"   Longitud          : {length}")
print(f"   Combinaciones     : {combinaciones}")
print("-" * 45)
print(f"   ¿Supera 1 billón? : {es_segura}")
print("=" * 45)