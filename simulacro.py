'''
Maximo Marzetti
una concesionaria nos pide un programa que nos permita cargar los datos de sus ventas:
las ventas son indeterminadas.

nombre del cliente:
edad(debe ser mayor)
marca del vehiculo (renault,fiat,bmw)
cantidad de puertas (2,4)
apellido del vendedor (Zapata,Quiroz,Simino)

se necesita saber:

A-Cantidad de vehiculos de 2 puertas que sean de la marca renault
B-nombre del cliente mas joven
C-porcentaje cada marca de auto sobre el total
D-promedio de edades de los clientes que compraron 4 puertas
E-nombre del cliente mas viejo que compro fiat
F-total de autos vendidos de la marca BMW
G-Apellido del vendedor que menos vendio
'''
contador_autos_dos_puertas_reno = 0

edad_minima = 0 
bandera_mas_joven = True

total_ventas = 0
contador_renault = 0
contador_fiat = 0
contador_bmw = 0

edad_maxima_fiat = 0
bandera_mas_viejo_fiat = 0

contador_clientes_cuatro_puertas = 0
acumulador_edades_cuatro_puertas = 0

contador_zapata = 0
contador_quiroz = 0
contador_simino = 0

while True:
    nombre_cliente = input('Nombre del cliente: ')
    
    edad_cliente = int(input('Edad del cliente (+18): '))
    while edad_cliente < 18: 
        edad_cliente = int(input('Edad no valida. Vuelva a ingresar la edad (+18): '))
    
    marca_auto = input('Marca del producto (renault, fiat, bmw): ')
    while marca_auto != 'renault' and marca_auto != 'fiat' and marca_auto != 'bmw':
        marca_auto = input('Error. La marca no es valida. Vuelva a ingresarla (renault, fiat, bmw): ')
    
    cantidad_puertas = int(input('Cantidad de puertas del vehiculo (2 / 4): '))
    while cantidad_puertas != 2 and cantidad_puertas != 4:
        cantidad_puertas = int(input('Error, vuelva a ingresar cantidad de puertas del vehiculo (2 / 4): '))
    
    apellido_vendedor = input('Ingrese el apellido del vendedor (Zapata, Quiroz, Simino): ')
    while apellido_vendedor != 'Zapata' and apellido_vendedor != 'Quiroz' and apellido_vendedor != 'Simino':
        apellido_vendedor = input('Error, vuelva a ingresar el apellido del vendedor (Zapata, Quiroz, Simino): ')
    #cantidad de vehiculos de 2 puertas que sean de la marca renault
    if marca_auto == 'renault' and cantidad_puertas == 2:
        contador_autos_dos_puertas_reno += 1
        
    #nombre cliente mas joven 
    if edad_cliente < edad_minima or bandera_mas_joven:
        edad_minima = edad_cliente
        cliente_mas_joven = nombre_cliente
        bandera_mas_joven = False
        
    #contando las marcas
    if marca_auto == 'renault':
        contador_renault += 1
    elif marca_auto == 'fiat':
        contador_fiat += 1
        #nombre cliente mas viejo de fiat
        if edad_cliente > edad_maxima_fiat or bandera_mas_viejo_fiat:
            edad_maxima_fiat = edad_cliente
            cliente_mas_viejo_fiat = nombre_cliente
            bandera_mas_viejo_fiat = False
    else:
        #F-total autos bmw
        contador_bmw += 1
        
    if cantidad_puertas == 4:
        contador_clientes_cuatro_puertas += 1
        acumulador_edades_cuatro_puertas += edad_cliente
        
    #contando las ventas de cada vendedor
    if apellido_vendedor == 'Zapata':
        contador_zapata += 1
    elif apellido_vendedor == 'Quiroz':
        contador_quiroz += 1
    else:
        contador_simino += 1
    
    print('-'*50)
    total_ventas += 1    
        
    pregunta = input('Desea cargar otra venta (si/no): ')
    if pregunta == 'no':
        break

#total_ventas = contador_renault + contador_fiat + contador_bmw
if contador_clientes_cuatro_puertas < 0:
    promedio_edad_clientes_cuatro_puertas = acumulador_edades_cuatro_puertas / contador_clientes_cuatro_puertas
else:
    promedio_edad_clientes_cuatro_puertas = 0

#porcentajes de ventas cada marca
porcentaje_renault = (contador_renault / total_ventas ) * 100
porcentaje_fiat = (contador_fiat / total_ventas ) * 100
porcentaje_bmw = (contador_bmw / total_ventas ) * 100

#G-Apellido del vendedor que menos vendio
if contador_zapata < contador_quiroz and contador_zapata < contador_simino:
    apellido_vendedor_menos_ventas = 'Zapata'
elif contador_quiroz < contador_simino:
    apellido_vendedor_menos_ventas = 'Quiroz'
else:
    apellido_vendedor_menos_ventas = 'Simino'

print(f'''
A-Cantidad de vehiculos de 2 puertas que sean de la marca renault: {contador_autos_dos_puertas_reno}
B-nombre del cliente mas joven: {cliente_mas_joven}
C-porcentaje cada marca de auto sobre el total: Renault: {porcentaje_renault:.2f}%, Fiat: {porcentaje_fiat:.2f}%, BMW: {porcentaje_bmw:.2f}%. 
D-promedio de edades de los clientes que compraron 4 puertas: {promedio_edad_clientes_cuatro_puertas} años.
E-nombre del cliente mas viejo que compro fiat: {cliente_mas_viejo_fiat}.
F-total de autos vendidos de la marca BMW: {contador_bmw} autos.
G-Apellido del vendedor que menos vendio: {apellido_vendedor_menos_ventas}.
      ''')