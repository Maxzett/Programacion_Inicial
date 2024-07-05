'''
1) Escribe un programa muestre por consola “Hola UTN”.
2) Escribe un programa que muestre por consola el resultado de sumar 3 + 5.
3) Escribe un programa que muestre por consola el resultado de restar 10-5
4) Escribe un programa que muestre por consola el resultado de restar 10-15
5) Escribe un programa que muestre por consola el resultado de multiplicar
4*10
6) Escribe un programa que muestre por consola el resultado de dividir 10/2
7) Escribe un programa que muestre por consola el resultado de dividir 10/0,
detalla en comentarios qué es lo que sucede al dividir por 0.
8) Escribe un programa que muestre por consola el resultado de la siguiente
operación (10+3) * (6+6), ¿qué sucede si realizas la misma operación pero sin
los paréntesis?
9) Escribe un programa que muestre por consola el resultado de la siguiente
operación 10%2
10) Escribe un programa que muestre por consola la siguiente operación 10%3
11) Crear un programa (suma, resta, multiplicación, y división),
se deberá generar dos variables del tipo “variableA” y “variableB”,
asignarles un valor del tipo número a cada una de ellas.
El programa deberá mostrar por consola el resultado de realizar las 4
operaciones aritméticas mencionadas entre ellas.

'''

#1
print('Hola UTN')
#2
print(3+5)
#3
print(10-5)
#4
print(10-15)
#5
print(4*10)
#6
print(10/2)
#7
#print(10/0)
#8
print((10+3)*(6+6))
#9
print(10%2)
#10
print(10%3)
#11
A = int(input('Inserte numero A: '))
B = int(input('Inserte numero B: '))
suma = A + B
resta = A - B 
multiplicacion = A * B
division = A/B
print(suma, resta, multiplicacion, division)