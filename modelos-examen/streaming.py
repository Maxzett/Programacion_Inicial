'''
Una empresa internacional está realizando un estudio de mercado para decidir cuál será la nueva plataforma de entretenimiento que se lanzará en el mercado argentino y en la cual invertirán.
Las posibles franquicias son las siguientes: Hulu, Vix+ o CODA.

Para ello, se realizará una encuesta mediante un sistema de voto electrónico, con el propósito de conocer cuáles son los gustos de los encuestados (no se sabe cuántos):
Se ingresa de cada encuestado:

Nombre
Edad (no menor a 18)
Tiene suscripción a algún servicio de streaming (sí-no)
Género (Masculino - Femenino - No binario - Otro)
Voto (Hulu, Vix+, CODA)
Se solicita realizar las siguientes búsquedas:

1. Cantidad de encuestados de género Masculino, cuya edad esté entre 18 y 25 o entre 36 y 49  que votaron por Hulu.
2. Nombre, género y edad del encuestado de menor edad que votó por Hulu.
3. Hallar el porcentaje de encuestados mayores de 25 años que tienen suscripción CODA.
4. Determinar el promedio de edad de los encuestados que votaron por Vix+.
5. Contar cuántos encuestados votaron por cada franquicia y determinar cual tuvo mas votos.
'''

bandera_menor_edad = True
edad_minima = 0

contador_hulu = 0

contador_subs_coda = 0
contador_subs_coda_mas_25 = 0

acumulador_edad_vix = 0
contador_vix = 0

contador_total_hulu = 0
contador_coda = 0

while True:
    #entradas
    nombre = input('Ingrese su nombre: ')
    
    edad = int(input('Ingrese su edad: '))
    while edad < 18:
        edad = int(input('Reingrese su edad: '))
    
    suscripcion = input('Tiene algun servicio de streaming (si/no)')
    while suscripcion != 'si' and suscripcion != 'no':
        suscripcion = input('Error. Vuelva a responder, tiene algun servicio de streaming (si/no)')
    
    genero = input('Ingrese su genero (masculino / femenino / no binario / otro): ')
    while genero != 'masculino' and genero != 'femenino' and genero != 'no binario' and genero != 'otro':
        genero = input('Vuleva a ingresar su genero (masculino / femenino / no binario / otro): ')
    
    voto = input('Voto (Hulu / Vix+ / CODA ): ')
    while voto != 'Hulu' and voto != 'Vix+' and voto != 'CODA':
        voto = input('Vuelva a ingresar su voto (Hulu / Vix+ / CODA ): ')
        
    #procesos
    
    if voto == 'Hulu':
        contador_total_hulu += 1
        #encuestado menor de edad que voto Hulu
        if edad < edad_minima or bandera_menor_edad:
            edad_minima = edad
            nombre_menor_edad = nombre            
            genero_menor_edad = genero
            menor_edad = edad
            bandera_menor_edad = False

        if genero == 'masculino':
            if edad >= 18 and edad <= 25:
                contador_hulu += 1
            elif edad >= 36 and edad <= 49:
                contador_hulu += 1
    elif voto == 'Vix+':
        contador_vix += 1
        acumulador_edad_vix += edad
    else:
        contador_coda += 1
        if suscripcion == 'si':
            contador_subs_coda += 1
        if edad > 25:
            contador_subs_coda_mas_25 += 1
            
    #salida de bucle
    pregunta = input('Desea cargar otro avistamiento (si/no): ')
    if pregunta == 'no':
        break
    
    porcentaje = (contador_subs_coda_mas_25 / contador_subs_coda) * 100
    
    if contador_vix != 0:
        promedio_vix = acumulador_edad_vix / contador_vix
    else:
        promedio_vix = 0
        
    #falta calcular el mas votado