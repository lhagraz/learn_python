#**Ejercicio 2 — Calculadora de subredes**
'''El usuario ingresa el número de hosts necesarios en una subred. 
Calcula y muestra cuántos bits se necesitan para representar esa cantidad de hosts 
(usa logaritmo base 2 aproximado con potencias de 2), y cuál es el rango total de IPs 
disponibles con ese número de bits. Pista: investiga cómo usar `2 ** n` para encontrar 
el valor mínimo mayor al número ingresado.
'''
cantidad_host = int(input("Ingrese la cantidad de hosts necesarios: "))

bits = 1
total_ips = 2 ** bits

while total_ips < cantidad_host:
    bits += 1
    total_ips = 2 ** bits
    
host_utilizables = total_ips - 2


print("=" * 40) 
print(f"Bits necesarios: {bits}")  
print(f"IPs totales en subred: {total_ips}")  
print(f"Host utilizables: {host_utilizables}")  
print("=" * 40) 