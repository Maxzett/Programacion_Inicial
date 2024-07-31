#Maximo Marzetti
'''
UTN Inversiones, realiza un estudio de mercado para saber cuál será la nueva
franquicia que se insertará en el mercado argentino y en la cual invertirán.
Las posibles franquicias son las siguientes: Apple, Dunkin o Ikea.
Para ello, se realizará una encuesta mediante un sistema de voto electrónico, con el
propósito de conocer cuáles son los gustos de los encuestados (no se sabe cuántos):
Se ingresa de cada encuestado:
● nombre
● edad (no menor a 18)
● está empleado (si-no)
● género (Masculino - Femenino - Otro)
● voto (APPLE, DUNKIN, IKEA)
Se necesita saber:
1. Cantidad de encuestados empleados que votaron por IKEA o APPLE, cuya
edad no supere los 36 años.
2. Nombre y voto del encuestado de género Femenino con mayor edad.
3. Porcentaje de encuestados de género Otro que votaron por DUNKIN.
4. Edad promedio de cada género.
5. Determinar cuál fue el género que tuvo menos encuestados.
'''

cont_empleados_distinto_dunkin = 0 

contador_femenino = 0
contador_masculino = 0
contador_otro = 0

acumulador_femenino = 0
acumulador_masculino = 0
acumulador_otro = 0

contador_dunkin_otro = 0

max_edad = 0
bandera_max_edad = True

while True:
    #entradas
    nombre = input('Ingrese su nombre: ')
    
    edad = int(input('Ingrese su edad(+18): '))
    while edad < 18:
        edad = int(input('Reingrese su edad: '))
    
    empleado = input('Esta empleado ? (si/no): ')
    while empleado != 'si' and empleado != 'no':
        empleado = input('Error. Vuelva a responder, esta empleado. (si/no): ')
    
    genero = input('Ingrese su genero (masculino / femenino / otro): ')
    while genero != 'masculino' and genero != 'femenino' and genero != 'otro':
        genero = input('Vuleva a ingresar su genero (masculino / femenino / otro): ')
    
    voto = input('Ingrese su voto (apple, dunkin, ikea): ')
    while voto != 'apple' and voto != 'dunkin' and voto != 'ikea':
        voto = input('Vuelva a ingresar su voto (apple, dunkin, ikea): ')
        
    #procesos
    if genero == 'femenino':
        contador_femenino += 1
        acumulador_femenino += edad
        #mayor de edad femenina
        if edad > max_edad or bandera_max_edad:
            max_edad = edad
            nombre_femenina_mayor = nombre
            voto_femenina_mayor = voto
            bandera_max_edad = False
        
    elif genero == 'masculino':
        contador_masculino += 1
        acumulador_masculino += edad
        
    else: #genero otro
        contador_otro += 1
        acumulador_otro += edad
        if voto == 'DUNKIN':
            contador_dunkin_otro += 1
    
    #empleado que no voto dunkin menor 36
    if empleado == 'si':
        if voto != 'DUNKIN' and edad <= 36:
            cont_empleados_distinto_dunkin += 1
    
    #salida de bucle
    pregunta = input('Desea cargar otra encuesta ? (si/no): ')
    if pregunta == 'no':
        break

#validacion otro igual a cero
if contador_otro == 0 or contador_dunkin_otro == 0:
    porcentaje = 0
else:
    porcentaje = (contador_otro / contador_dunkin_otro) * 100

#edades promedios por genero
if contador_femenino > 0:
    promedio_femenino = acumulador_femenino / contador_femenino
else:
    promedio_femenino = 0
if contador_masculino > 0:
    promedio_masculino = acumulador_masculino / contador_masculino
else:
    promedio_masculino = 0
if contador_otro > 0:
    promedio_otro = acumulador_otro / contador_otro
else:
    promedio_otro = 0
    
#genero con menos votos
if contador_femenino < contador_masculino and contador_femenino < contador_otro:
    genero_menos_encuestado = 'FEMENINO'
elif contador_masculino < contador_otro:
    genero_menos_encuestado = 'MASCULINO'
else:
    genero_menos_encuestado = 'OTRO'

#validacion femenina mayor
if contador_femenino == 0:
    nombre_femenina_mayor = 'NADIE'
    voto_femenina_mayor = 'NADIE'
    
#salidas
print(f'''
La cantidad de encuestados empleados que votaron por IKEA o APPLE, cuya edad no supera los 36 años es de {cont_empleados_distinto_dunkin} personas.
La encuestada de género Femenino con mayor edad fue: {nombre_femenina_mayor} su voto fue para: {voto_femenina_mayor}.
El porcentaje de encuestados de género Otro que votaron por DUNKIN es de {porcentaje:.2f}%.
El promedio de edad del genero FEMENINO es de {promedio_femenino:.2f} años, el del genero MASCULINO es de {promedio_masculino:.2f} años y el del genero OTRO es de {promedio_otro:.2f} años.
El genero que tuvo menos cantidad de encuestados fue el genero: {genero_menos_encuestado}.
      ''')