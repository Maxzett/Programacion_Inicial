#Maximo Marzetti
'''
Ejercicio 7
Pedirle al usuario su edad, determinar si es mayor (18 años o más), niño/a (menor de 10), pre-adolescente (edad entre 10 y 13 años inclusive) o adolescente (edad entre 13 y 17 años).
'''

numero = int(input('Ingrese un numero: '))
if numero < 10:
    print('Sos un nino/a')
elif numero >= 10 and numero <= 13:
    print('Sos un pre-adolescente') 
elif numero > 13 and numero <= 17:
    print('Sos adolescente')
else:
    print('Sos mayor')