'''
Ejercicio 11
Pedir al usuario el ingreso de una nota. La misma debe estar comprendida entre 1 y 10 inclusive.
'''


'''
nota = int(input('Ingrese una nota(entre 1 y 10): '))

while nota < 1 or nota > 10:
    print('Error.')
    nota = int(input('Ingrese una nota(entre 1 y 10): '))
    
print(f'Su nota es {nota}')
'''

while True:
    nota = int(input('Ingrese una nota(entre 1 y 10): '))
    
    if nota >= 1 and nota <= 10:
        break
    
    nota = int(input('Error. Reingrese la nota(entre 1 y 10): '))
    
print(f'Su nota es {nota}')