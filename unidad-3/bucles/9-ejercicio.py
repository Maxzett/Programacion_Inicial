'''
Maximo Marzetti
Ejercicio 9
Pedir el ingreso de una clave. Validar que el ingreso del usuario sea correcto. Tendrá intentos indeterminados.
'''

clave = input('Ingrese la clave: ')

while True:
    if clave == 'utn123':
        break
    clave = input('Incorrecta. Ingrese la clave: ')

if clave == 'utn123':
    print('Clave correcta.')
