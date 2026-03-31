#**Ejercicio 8 — Parseador de URL**
'''El usuario ingresa una URL completa como `https://empresa.com:8443/login?user=admin`. 
Extrae y muestra por separado: el protocolo (`https`), el dominio (`empresa.com`), el puerto
 (`8443`), la ruta (`/login`), y los parámetros (`user=admin`). Usa únicamente métodos de strings. 
 Asume que la URL siempre tiene ese formato.
'''
url = input("Ingrese la url: ")
items = url.split("/")
protocolo = url.split(":")[0]
dominio, puerto = items[2].split(":")
ruta, parametros = items[3].split("?")

print("\n" + "=" * 45)
print("             PARSEADOR DE URL")
print("=" * 45)
print(f"Protocolo   : {protocolo}")
print(f"Dominio     : {dominio}")
print(f"Puerto      : {puerto}")
print(f"Ruta        : /{ruta}")
print(f"Parámetros  : {parametros}")
print("=" * 45)