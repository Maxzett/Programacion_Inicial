#Maximo Marzetti
'''
Ejercicio 6
Pedirle al usuario su edad, determinar si el usuario NO es adolescente.
'''
age = int(input('Ingrese su edad: '))
if age < 13 or age > 17:
    print('NO sos un adolescente')