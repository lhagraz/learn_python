#Ejercicio 2 — Sistema de autenticación básico
'''Simula un sistema de login con máximo 3 intentos. El usuario ingresa un nombre 
de usuario y contraseña. Si coinciden con los valores correctos (admin / cyb3rs3c), 
imprime acceso concedido y termina. Si falla, cuenta el intento y avisa cuántos le quedan. 
Al agotar los 3 intentos, imprime que la cuenta fue bloqueada. Usa while y break.'''

valor_user = "admin"
valor_passw = "cyb3rs3c"

print("=" * 45)
print("                AUTENTICACIÓN")
print("=" * 45)
    
contador = 3
while contador != 0:
    user = input("Ingrese nombre de usuario: ")
    passw = input("Ingrese contraseña: ")

    if user == valor_user and passw == valor_passw:
        print("  [OK] Acceso concedido — Bienvenido")
        
        break
    else:
        contador -= 1
        print("  [ERROR] Usuario o contraseña inválidos")
        print(f"  Intentos restantes : {contador}")

    if contador == 0:
        print("  [BLOQUEADO] Cuenta bloqueada — acceso denegado")