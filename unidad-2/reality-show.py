'''
Enunciado:
De los 3 Jugadores de un Reality Show, se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibió en la etapa de votos
Informar:
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan mediante input()
'''

cont = 0
cant_participantes = 3
mas_votos = 0
nombre_mas_votos = ''
menos_votos = float('inf')
nombre_menos_votos = ''
edad_menos_votos = 0
suma_edades = 0
total_votos = 0

while cont < cant_participantes:
    nombre = str(input('Nombre participante: '))
    edad = int(input('Edad participante: '))
    while edad < 25:
        edad = int(input('Ingrese nuevamente la edad: '))
    votos = int(input('Votos del participante: '))
    while votos <= 0:
        votos = int(input('Ingrese nuevamente los votos: '))
        
    if votos > mas_votos:
        mas_votos = votos
        nombre_mas_votos = nombre
        
    if votos < menos_votos:
        menos_votos = votos
        nombre_menos_votos = nombre
        edad_menos_votos = edad     

    suma_edades += edad
    total_votos += votos
    print('-'*30)
    cont += 1

promedio_edades = suma_edades//cant_participantes

print(f"a. Nombre del participante con mas votos: {nombre_mas_votos}")
print(f"b. Nombre y edad del participante con menos votos: {nombre_menos_votos}, {edad_menos_votos} años")
print(f"c. Promedio de edades de los participantes: {promedio_edades} años")
print(f"d. Total de votos: {total_votos} votos")