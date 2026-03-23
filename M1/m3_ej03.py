# **Ejercicio 3 — Analizador de banner**
'''Dado el string `"SSH-2.0-OpenSSH_8.2p1 Ubuntu-4ubuntu0.5"`, extrae y muestra por separado:
 el protocolo (`SSH`), la versión del protocolo (`2.0`), el software (`OpenSSH`), y la versión
   del software (`8.2p1`). Usa únicamente operaciones de strings (slicing, split, índices).
'''
banner = "SSH-2.0-OpenSSH_8.2p1 Ubuntu-4ubuntu0.5"

datos = banner.split("-")
datos_software = datos[2].split("_")

print("=" * 40)
print("Características del banner")
print("=" * 40)
print(f"""Protocolo: {datos[0]} 
Versión del protocolo: {datos[1]}
Software: {datos_software[0]}
Versión software: {datos_software[1].split(" ")[0]}""")
print("=" * 40)


