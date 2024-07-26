'''
Maximo Marzetti
una fabrica nos pide un programa que nos permita cargar los datos de sus ventas:
las ventas no son siempre las mismas.

nombre del cliente:
edad(debe ser mayor)
Precio(mayor a 1000)
marca del producto (dream,patito,lenovo)
nombre del vendedor (Jose,Pepe,Juan)

se necesita saber:

A-Cantidad de Productos, que tengan el precio mayor a 2000 y que no sean de la marca dream
B-nombre del cliente mas viejo
C-porcentaje cada marca sobre el total
D-promedio de precio de los clientes que compraron marca patito
'''
cantidad_productos = 0
#B-nombre del cliente mas viejo
edad_maxima = 0
flag_cliente_mas_viejo = True
nombre_mas_viejo = ''
#C-porcentaje cada marca sobre el total
total_ventas = 0
contador_dream = 0
# contador_patito = 0
contador_lenovo = 0
#D-promedio de precio de los clientes que compraron marca patito
acumulador_precio_patito = 0
contador_compras_patito = 0


while True:
    nombre_cliente = input('Nombre del cliente: ')
    
    edad_cliente = int(input('Edad del cliente (+18): '))
    while edad_cliente < 18: 
        edad_cliente = int(input('Edad no valida. Vuelva a ingresar la edad (+18): '))

    precio = int(input('Precio del producto (mayor a 1000): '))
    while precio < 1000:
        precio = int(input('Vuelva a ingresar el precio del producto: '))
        
    marca_producto = input('Marca del producto (dream, patito, lenovo): ')
    while marca_producto != 'dream' and marca_producto != 'patito' and marca_producto != 'lenovo':
        marca_producto = input('Error. La marca no valida. Vuelva a ingresarla (dream, patito, lenovo): ')
        
    nombre_vendedor = input('Ingrese el nombre del vendedor (Jose, Pepe, Juan): ')
    while nombre_vendedor != 'Jose' and nombre_vendedor != 'Pepe' and nombre_vendedor != 'Juan':
        nombre_vendedor = input('Error. Ingrese de nuevo el nombre del vendedor (Jose, Pepe, Juan): ')
    
    if marca_producto != 'dream' and precio > 2000:
        cantidad_productos += 1
    
    if edad_cliente > edad_maxima or flag_cliente_mas_viejo == True:
        edad_maxima = edad_cliente
        nombre_mas_viejo = nombre_cliente
        flag_cliente_mas_viejo = False
        
    if marca_producto == 'patito':
        contador_compras_patito += 1
        acumulador_precio_patito += precio    
    elif marca_producto == 'dream':
        contador_dream += 1
    else:
        contador_lenovo += 1
    
    print('-'*50)
    total_ventas += 1
        
    pregunta = input('Desea cargar otra venta (si/no): ')
    if pregunta == 'no':
        break

promedio_precio_patito = acumulador_precio_patito // contador_compras_patito

porcentaje_patito = (contador_compras_patito / total_ventas) * 100
porcentaje_patito = int(porcentaje_patito)
porcentaje_dream = (contador_dream / total_ventas) * 100
porcentaje_dream = int(porcentaje_dream)
porcentaje_lenovo = (contador_lenovo / total_ventas) * 100
porcentaje_lenovo = int(porcentaje_lenovo)

print(f'''
A-Cantidad de Productos, que tengan el precio mayor a 2000 y que no sean de la marca dream: {cantidad_productos}
B-nombre del cliente mas viejo: {nombre_mas_viejo}
C-porcentaje cada marca sobre el total: patito = {porcentaje_patito}%, dream = {porcentaje_dream}%, lenovo = {porcentaje_lenovo}%
D-promedio de precio de los clientes que compraron marca patito: {promedio_precio_patito}
      ''')