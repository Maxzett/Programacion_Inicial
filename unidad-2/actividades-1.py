'''
1) Crear un programa que pida al usuario un número, si coincide con el valor
18, mostrar el mensaje “Usted tiene 18 años”.
2) Crear un programa que pida al usuario un número y pueda calcular si es o
no mayor de edad. Si es mayor de 18 se mostrará el mensaje “MAYOR” caso
contrario “MENOR”.
3) Crear un programa que a partir del ingreso de la altura de un
basquetbolista determinar si es pivot o no. Para serlo el mismo deberá
medir más de 1.80 metros
4) Crear un programa que se ingrese la edad del usuario en número y pueda
calcular si es adolescente (edad entre 13 y 17 años).
5) Crear un programa que al ingresar un número puede calcular si es mayor,
niño/a(menor de 10) o pre-adolescente (edad entre 10 y 13 años)
adolescente (edad entre 13 y 17 años) de edad.
'''
#1
# num = int(input('Ingrese un numero: '))
# if num == 18:
#     print('Usted tiene 18 años')

#2
# edad = int(input('Ingrese su edad: '))
# if edad >= 18:
#     print('Usted es MAYOR de edad')
# else:
#     print('Usted es MENOR de edad')
        
#3
# altura = float(input('Ingresa tu estatura: '))
# if altura > 1.80:
#     print('Sos pivot')
# else: 
#     print('No sos pivot')

#4
# age = int(input('Introduzca su edad en numeros: '))
# if age >= 13:
#     if age <= 17:
#         print('Sos un adolescente')

#5        
numero = int(input('Ingrese un numero: '))
if numero < 10:
    print('Sos un nino/a')
elif numero >= 10 and numero <= 13:
    print('Sos un pre-adolescente') 
elif numero > 13 and numero <= 17:
    print('Sos adolescente')
else:
    print('Sos mayor')