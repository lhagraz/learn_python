#**Ejercicio 10 — Informe de reconocimiento**
'''Integra lo aprendido: solicita al usuario mediante `input()` 
los siguientes datos de un objetivo: IP, dominio, sistema operativo,
 versión del SO, puerto principal, y si tiene firewall activo 
 (el usuario escribe `"si"` o `"no"`). Almacena todo en variables correctamente 
 tipadas y genera un informe formateado con f-strings que simule la salida de una 
 herramienta de reconocimiento profesional. El informe debe tener encabezado, 
 separadores visuales con `=` o `-`, y cada campo en su propia línea etiquetada.
'''
ip = input("Ingrese IP objetivo: ")
dominio = input("Ingrese dominio: ")
sistema_op = input("Ingrese sistema operativo: ")
version_so = input("Ingrese versión del SO: ")
puerto = int(input("Ingrese puerto principal: "))
firewall = input("¿Tiene firewall activo? (si/no): ")
estado_firewall = "Activo" if firewall == "si" else "Inactivo"

print("\n" + "=" * 45)
print("          INFORME DE RECONOCIMIENTO")
print("=" * 45)
print(f"""
      IP                : {ip}
      DOMINIO           : {dominio}                
      SISTEMA OPERATIVO : {sistema_op}                
      VERSIÓN SO         : {version_so}       
      PUERTO PRINCIPAL  : {puerto}               
      FIREWALL          : {estado_firewall}                 
""")
print("=" * 45)