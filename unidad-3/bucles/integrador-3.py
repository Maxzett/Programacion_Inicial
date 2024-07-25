'''
Maximo Marzetti
Validaciones.
Una empresa dedicada a la toma de datos para realizar estadísticas y censos, nos pide realizar la carga y validación de datos para luego mostrarlos por pantalla. 
Los datos requeridos son:
Apellido
Edad, entre 18 y 90 años inclusive.
Estado civil: “Soltero/a”, ”Casado/a”, “Divorciado/a” o “Viudo/a”.
Número de legajo: valor numérico de 4 cifras, sin ceros a la izquierda.
'''

apellido = str(input('Ingrese su apellido: '))

edad = int(input('Ingrese su edad(Valida entre 18 y 90 años): '))
while edad < 18 or edad > 90:
    print('Edad no valida')
    edad = int(input('Ingrese su edad(Valida entre 18 y 90 años): '))

estado_civil = input('Ingrese su estado civil: "Soltero/a", "Casado/a", "Divorciado/a" o "Viudo/a".  ')
while True:
    if estado_civil == 'Soltero' or estado_civil =='Casado' or estado_civil == 'Divorciado' or estado_civil == 'Viudo':
        break
    else:
        estado_civil = input('Error. Vuelva a intentarlo. Ingrese su estado civil: "Soltero/a", "Casado/a", "Divorciado/a" o "Viudo/a".  ')
    
num_legajo = int(input('Ingrese su numero de legajo(valor numérico de 4 cifras, sin ceros a la izquierda): '))
while True:
    if num_legajo > 1000 and num_legajo < 9999:
        break
    else: 
       print('Error de numero de legajo.')  
       num_legajo = int(input('Ingrese su numero de legajo(valor numérico de 4 cifras, sin ceros a la izquierda): '))