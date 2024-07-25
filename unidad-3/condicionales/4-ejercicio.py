#Maximo MArzetti
'''
Ejercicio 4
A partir del ingreso de la altura de un basquetbolista determinar si es pivot o no. Para serlo el mismo deberá medir más de 1.80 metros.
'''
altura = float(input('Ingresa tu estatura: '))
if altura > 1.80:
    print('Sos pivot')
else: 
    print('No sos pivot')