#**Ejercicio 5 — Conversor de unidades de datos**
'''El usuario ingresa un tamaño en bytes. El programa debe mostrar ese valor convertido a: 
Kilobytes (KB), Megabytes (MB), Gigabytes (GB) y
 Terabytes (TB). Usa división y redondea a 4 decimales con 
 `round()`. Esto es útil al analizar tamaño de archivos capturados en una auditoría.
'''
tamaño_bytes = int(input("Ingrese tamaño a convertir en bytes: "))


tamaño_kb = tamaño_bytes / 1024
tamaño_mb = tamaño_kb / 1024
tamaño_gb = tamaño_mb / 1024
tamaño_tb = tamaño_gb / 1024


print("\n" + "=" * 45)
print("     CONVERSOR DE UNIDADES DE DATOS")
print("=" * 45)
print(f"Bytes     : {tamaño_bytes}B")
print(f"Kilobytes : {round(tamaño_kb, 4)}KB")
print(f"Megabytes : {round(tamaño_mb, 4)}MB")
print(f"Gigabytes : {round(tamaño_gb, 4)}GB")
print(f"Terabytes : {round(tamaño_tb, 4)}TB")
print("=" * 45)