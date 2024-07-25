'''
Maximo Marzetti
Ejercicio 12
Solicitarle al usuario el ingreso de un color primario. Validar que el mismo sea Rojo, Verde o Azul.
'''

while True:
    color = input('Ingrese un color primario: ')
    
    if color == 'rojo' or color == 'verde' or color == 'azul':
        print('Es un color primario.')
        break
    else:
        print('El color ingresado NO es primario.')