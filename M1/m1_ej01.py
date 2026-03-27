# **Ejercicio 1 — Variables de reconocimiento**
'''Declara variables para almacenar los datos típicos de un objetivo de reconocimiento: dirección IP, nombre de 
dominio, sistema operativo detectado, número de puertos abiertos y si el host está activo. Imprime cada variable 
con una etiqueta descriptiva usando f-strings.'''
direccion_ip = "192.168.1.105"
dominio = "servidor-interno.empresa.com"
sistema_op = "Windows Server 2019" 
nro_puertos = 5
estado_host = False
estado_legible = "Activo" if estado_host else "Inactivo"

print("=" * 60)
print("                      RECONOCIMIENTO")
print("=" * 60)
print(f"""                    Datos del objetivo
   Dirección IP              : {direccion_ip}
   Dominio                   : {dominio}
   Sistema operativo         : {sistema_op}
   Número de puertos abiertos: {nro_puertos}
   Estado del host           : {estado_legible}""")
print("=" * 60)