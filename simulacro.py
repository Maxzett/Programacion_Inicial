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
cliente_mas_joven = ''

total_ventas = 0
contador_renault = 0
contador_fiat = 0
contador_bmw = 0

edad_maxima_fiat = 0
bandera_mas_viejo_fiat = 0
cliente_mas_viejo_fiat = ''

menos_ventas = 0
bandera_menos_ventas = True
apellido_vendedor_menos_ventas = ''

contador_clientes_cuatro_puertas = 0
acumulador_edades_cuatro_puertas = 0

contador_ventas = 0

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
    contador_ventas += 1
    
    if marca_auto == 'renault' and cantidad_puertas == 2:
        contador_autos_dos_puertas_reno += 1
    #nombre cliente mas joven 
    if edad_cliente < edad_minima or bandera_mas_joven == True:
        edad_cliente = edad_minima
        cliente_mas_joven = nombre_cliente
        bandera_mas_joven = False
    
    if marca_auto == 'renault':
        contador_renault += 1
    elif marca_auto == 'fiat':
        contador_fiat += 1
        #nombre cliente mas viejo de fiat
        if edad_cliente > edad_maxima_fiat or bandera_mas_viejo_fiat == True:
            edad_cliente = edad_maxima_fiat
            cliente_mas_viejo_fiat = nombre_cliente
            bandera_mas_viejo_fiat = False
    else:
        #F-total autos bmw
        contador_bmw += 1
        
    if cantidad_puertas == 4:
        contador_clientes_cuatro_puertas += 1
        acumulador_edades_cuatro_puertas += edad_cliente
    
    if contador_ventas < menos_ventas or bandera_menos_ventas == True:
        menos_ventas = contador_ventas
        apellido_vendedor_menos_ventas = apellido_vendedor
        bandera_menos_ventas = False
        
    print('-'*50)
    total_ventas += 1    
        
    pregunta = input('Desea cargar otra venta (si/no): ')
    if pregunta == 'no':
        break
    
promedio_edad_clientes_cuatro_puertas = acumulador_edades_cuatro_puertas / contador_clientes_cuatro_puertas

porcentaje_renault = (contador_renault / total_ventas ) * 100
porcentaje_fiat = (contador_fiat / total_ventas ) * 100
porcentaje_bmw = (contador_bmw / total_ventas ) * 100

print(f'''
A-Cantidad de vehiculos de 2 puertas que sean de la marca renault: {contador_autos_dos_puertas_reno}
B-nombre del cliente mas joven: {cliente_mas_joven}
C-porcentaje cada marca de auto sobre el total: Renault: {porcentaje_renault:.2f}%, Fiat: {porcentaje_fiat:.2f}%, BMW: {porcentaje_bmw:.2f}%. 
D-promedio de edades de los clientes que compraron 4 puertas: {promedio_edad_clientes_cuatro_puertas} años.
E-nombre del cliente mas viejo que compro fiat: {cliente_mas_viejo_fiat}.
F-total de autos vendidos de la marca BMW: {contador_bmw} autos.
G-Apellido del vendedor que menos vendio: {apellido_vendedor_menos_ventas}.
      ''')