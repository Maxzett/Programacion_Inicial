'''
Enunciado:
Para el departamento de facturación:
A. Ingresar tres precios de productos y mostrar la suma de los mismos.
B. Ingresar tres precios de productos y mostrar el promedio de los mismos.
C. ingresar tres precios de productos sumarlos y mostrar el precio final (más IVA 21%).
'''

producto_1 = int(input('Precio producto 1: $'))
producto_2 = int(input('Precio producto 2: $'))
producto_3 = int(input('Precio producto 3: $'))

precio_total = producto_1 + producto_2 + producto_3
iva = (precio_total * 21)/100

print(f'El precio total es: ${precio_total}')
print(f'El precio promedio es: ${precio_total//3}')
print(f'El precio final mas %IVA es: ${precio_total + iva}')