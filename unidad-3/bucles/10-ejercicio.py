'''
Maximo Marzetti
Ejercicio 10
intentos el ingreso de una clave. Validar que el ingreso del usuario sea correcto. Solo tendrá 3 intentos.
'''

intentos = 3

while True:
    clave = input('Ingrese su clave: ')

    if clave == 'utn103' or intentos == 1:
        break

    intentos -= 1

if clave == 'utn103':
    print('Contraseña correcta')
else:
    print('Contraseña incorrecta')