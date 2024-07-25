'''
Maximo Marzetti
Integrador.2
De los 20 jugadores participantes en un torneo de ajedrez, se registra:

nombre
la edad (mayor de 10 años)
la cantidad de partidas ganadas (no menor a cero) que obtuvieron en el torneo.

Informar:
a. Nombre del jugador con más partidas ganadas.
b. Nombre y edad del jugador con menos partidas ganadas.
c. El promedio de edades de los jugadores.
d. El total de partidas ganadas.
e. El jugador más joven.
'''
contador = 0
total_participantes = 20
total_partidas_ganadas = 0
#maximos
bandera_partidas_maximas = True
nombre_mas_partidas_ganadas = ''
partidas_ganadas_maximas = 0
#minimos
bandera_partidas_minimas = True
nombre_menos_partidas_ganadas = ''
edad_jugador_menos_partidas_ganadas = 0
partidas_ganadas_minimas = 0

suma_edades = 0
nombre_jugador_mas_joven = ''
edad_minima = 0
bandera_mas_joven = True


while contador < total_participantes:
    nombre = input('Ingrese su nombre: ')
    
    edad = int(input('Ingrese su edad(mayor a 10 años): '))
    while edad < 10:
        edad = int(input('Valor erroneo. Ingrese nuevamente la edad: '))
    
    partidas_ganadas = int(input('Ingrese la cantidad de partidas ganadas: '))
    while partidas_ganadas < 0:
        partidas_ganadas = int(input('Valor erroneo. Ingrese nuevamente la cantidad de partidas ganadas: '))
    
    #a. Nombre del jugador con más partidas ganadas.
    if partidas_ganadas > partidas_ganadas_maximas or bandera_partidas_maximas == True:
        partidas_ganadas_maximas = partidas_ganadas
        nombre_mas_partidas_ganadas = nombre
        bandera_partidas_maximas = False
    
    #b. Nombre y edad del jugador con menos partidas ganadas.
    if partidas_ganadas < partidas_ganadas_minimas or bandera_partidas_minimas == True:
        partidas_ganadas_minimas = partidas_ganadas
        nombre_menos_partidas_ganadas = nombre
        edad_jugador_menos_partidas_ganadas = edad
        bandera_partidas_minimas = False
    
    #e. El jugador más joven.
    if edad < edad_minima or bandera_mas_joven == True:
        edad_minima = edad
        nombre_jugador_mas_joven = nombre
        bandera_mas_joven = False
    
    suma_edades += edad
    #d. El total de partidas ganadas.
    total_partidas_ganadas += partidas_ganadas
    print('-'*30)
    contador += 1
    
#c. El promedio de edades de los jugadores.  
promedio_edades = suma_edades // total_participantes

print(f"""
a. Nombre del jugador con más partidas ganadas: {nombre_mas_partidas_ganadas}
b. Nombre y edad del jugador con menos partidas ganadas: {nombre_menos_partidas_ganadas} de {edad_jugador_menos_partidas_ganadas} años.
c. Promedio de edades de los jugadores: {promedio_edades} años.
d. Total de partidas ganadas: {total_partidas_ganadas}.
e. Jugador más joven: {nombre_jugador_mas_joven}
      """)