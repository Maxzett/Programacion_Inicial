'''
Como es de público conocimiento, la NASA reconoció que se han encontrado restos biológicos no humanos en otros planetas. Dada esta situación, y en su afán de blanquear tantos años de avistamientos desmentidos, nos piden que realicemos un programa que permita llevar un control de los mismos para mostrarlos a la sociedad. 

Por cada avistamiento se registra:
Nombre del empleado que notificó el avistamiento
Forma de la nave (Platillo, Esférica, Ovalada)
Velocidad máxima de la nave (mayor a 100 km/h)
Tipo de mensaje (Ninguno - Claro - Incomprensible) 
    
En esta opción el usuario podrá cargar avistamientos hasta que lo desee.

Se desea saber:
Velocidad promedio según la forma de la nave.
Porcentaje de avistamientos con algún tipo de mensaje, Siempre y cuando la velocidad se encuentre entre los 200 km/h y los 500 km/h.
Tipo de mensaje menos recibido.
Nombre del empleado y forma de la nave del avistamiento con mensajes Incomprensibles, de las naves que resultaron ser más rápidas.
Cantidad de avistamientos que superen los 250 Km/h, cuyo mensaje sea Claro o incomprensible y que sea de tipo Esférica.
Si por lo menos algún empleado se llama “Mercedes”
'''

contador_platilllo = 0
contador_esferica = 0
contador_ovalada = 0

acumulador_velocidad_platillo = 0
acumulador_velocidad_esferica = 0
acumulador_velocidad_ovalada = 0

contador_mensajes_velocidad_limitada = 0
contador_total_mensajes = 0

contador_claro = 0 
contador_incomprensible = 0 

contador_mas_250 = 0

nave_mas_rapida = 0
bandera_nave_mas_rapida = True

contador_mercedes = 0

while True:
    nombre = input('Ingrese el nombre del empleado que notificó el avistamiento: ')

    nave = input('Ingrese la forma de la nave (Platillo, Esférica, Ovalada): ')
    while nave != 'platillo' and nave != 'esferica' and nave != 'ovalada':
        nave = input('Reingrese la forma de la nave (Platillo, Esférica, Ovalada): ')

    velocidad_max_nave = int(input('Ingrese la velocidad máxima de la nave (mayor a 100 km/h): '))
    while velocidad_max_nave < 100:
        velocidad_max_nave = int(input('Reingrese la velocidad máxima de la nave (mayor a 100 km/h): '))

    tipo_mensaje = input('Ingrese tipo de mensaje (Ninguno - Claro - Incomprensible): ')
    while tipo_mensaje != 'ninguno' and tipo_mensaje != 'claro' and tipo_mensaje != 'incomprensible':
        tipo_mensaje = input('Reingrese el tipo de mensaje (Ninguno - Claro - Incomprensible): ')
    
    if nave == 'platillo':
        contador_platilllo += 1
        acumulador_velocidad_platillo += velocidad_max_nave    
    elif nave == 'esferica':
        contador_esferica += 1
        acumulador_velocidad_esferica += velocidad_max_nave
    else:
        contador_ovalada += 1
        acumulador_velocidad_ovalada += velocidad_max_nave

    #avistamientos con algun tipo de mensaje, entre velocidades 200 a 500
    if velocidad_max_nave > 200 and velocidad_max_nave < 500:
        contador_mensajes_velocidad_limitada += 1
        
    if tipo_mensaje != 'ninguno':
        if velocidad_max_nave > 250 and nave == 'esferica':
            contador_mas_250 += 1
        if tipo_mensaje == 'claro':
            contador_claro += 1
        else:
            contador_incomprensible += 1
          
    if nombre == 'Mercedes':
        contador_mercedes += 1
        
    #naves mas rapidas
    if velocidad_max_nave > nave_mas_rapida or bandera_nave_mas_rapida:
        nave_mas_rapida = velocidad_max_nave
        empleado_nave_mas_rapida = nombre
        tipo_nave_mas_rapida = nave
        bandera_nave_mas_rapida = False
    
    contador_total_mensajes += 1
    
    pregunta = input('Desea cargar otro avistamiento (si/no): ')
    if pregunta == 'no':
        break
    
#promedios velocidad segun tipo de nave
if contador_platilllo > 0:
    promedio_platillo = acumulador_velocidad_platillo / contador_platilllo
else:
    promedio_platillo = 0
promedio_esferica = acumulador_velocidad_esferica / contador_esferica
promedio_ovalada = acumulador_velocidad_ovalada / contador_ovalada

#tipo mensaje menos recibido
if contador_claro < contador_incomprensible:
    tipo_mensaje_menos_recibido = 'claro'
else:
    tipo_mensaje_menos_recibido = 'incomprensible'
    
#porcentaje
porcentaje = (contador_mensajes_velocidad_limitada / contador_total_mensajes) * 100
    
#Mercedes
if contador_mercedes >= 1:
    mercedes = 'Hay un empleado llamado Mercedes'
else:
    mercedes = 'No hay empleado de nombre Mercedes'
    
print(f'''
Velocidad promedio platillo: {promedio_platillo}
Velocidad promedio esferica: {promedio_esferica}
Velocidad promedio ovalada: {promedio_ovalada}
El porcentaje de avistamientos con algún tipo de mensaje, Siempre y cuando la velocidad se encuentre entre los 200 km/h y los 500 km/h, es de %{porcentaje}.
Tipo de mensaje menos recibido fue {tipo_mensaje_menos_recibido}
{empleado_nave_mas_rapida} vio la nave de tipo {tipo_nave_mas_rapida} con mensajes Incomprensibles y resulto ser la nave mas rapida.
{contador_mas_250} fueron la cantidad de avistamientos que superen los 250 Km/h, cuyo mensaje sea Claro o incomprensible y que sea de tipo Esférica.
{mercedes}
    ''')