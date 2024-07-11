'''
1) Crear un programa que pueda sumar los números pares comprendidos
entre el 1 y el 10.
2) Crear un programa que solicite al usuario que ingrese una contraseña
mediante prompt.
Comprobar que la contraseña ingresada sea "utn750". En caso de no
coincidir, volver a solicitarla hasta que coincidan.
3) Crear un programa que solicite al usuario que ingrese un número.
Se deberá validar que se encuentre entre 0 y 9 inclusive. En caso no
coincidir con el rango, volverlo a solicitar hasta que la condición se cumpla.
4) Crear un programa que solicite al usuario que ingrese una letra. Se deberá
validar que la letra sea "U", "T" o "N" (en mayusculas).
En caso no coincidir con ninguna de las letras, volver a solicitarla hasta que
la condición se cumpla.
5) Crear un programa que solicite 5 números mediante prompt. Calcular la
suma acumulada y el promedio de los números ingresados.
'''

#1
suma_pares = 0
for numero in range(1,11):
    if numero %2 == 0:
        suma_pares += numero
print(f'La suma de los números pares entre 1 y 10 es: {suma_pares}')

#2
password = input('Ingrese la contraseña: ')
while password != 'utn750':
    password = input('Vuelva a intentarlo: ')
print('Contraseña correcta!')

#3
num_usuario = int(input('Ingrese un numero entre el 0 y 9: '))
while num_usuario not in range(0,10):
    print('No cumple la consigna')
    num_usuario = int(input('Ingrese un numero entre el 0 y 9: '))
print('Gracias por cumplir la consigna') 

#4
letra_usuario = input('Ingrese una letra en mayuscula: ')
while letra_usuario not in ('U','T','N'):
    print('Letra Incorrecta')
    letra_usuario = input('Ingrese otra letra: ')
print(f'La letra {letra_usuario} es valida.')

#5
cont=0
suma_nums=0
while cont < 5:
    num = int(input('Inserte un numero: '))
    suma_nums = suma_nums + num    
    cont += 1
print(f'La suma total de los numeros es {suma_nums}')
print(f'El promedio es {suma_nums/5}')