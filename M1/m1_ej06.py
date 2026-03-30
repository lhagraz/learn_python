#**Ejercicio 6 — Generador de identificador de sesión**
'''Sin usar librerías externas, construye un string que simule un identificador
 de sesión concatenando: el nombre del usuario (input), el puerto de conexión (input, entero), 
 y el timestamp simulado `20240315120000`. Muestra el ID resultante, su longitud, y el mismo ID en mayúsculas. 
 Formato esperado: `admin_443_20240315120000`.
'''
usuario = input("Introduzca su usuario: ")
puerto = int(input("Ingrese su numero de puerto: "))
timestamp = "20240315120000"
id_resultante = (f"{usuario}_{puerto}_{timestamp}")

print("\n" + "=" * 45)
print("          IDENTIFICADOR DE SESIÓN")
print("=" * 45)
print(f"ID completo     : {id_resultante}") 
print(f"Longitud del ID : {len(id_resultante)}") 
print(f"ID en mayuscúla : {id_resultante.upper()}") 
print("=" * 45)
