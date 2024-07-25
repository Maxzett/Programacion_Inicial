'''
Maximo Marzetti
Ejercicio 8
Ingresar 10 números enteros. Determinar el máximo y el mínimo.
'''
contador = 0
numero_max = 0
numero_min = 0
flag_primer_numero = True

while contador < 10:
    numero = input('Ingrese un numero: ')
    
    '''
    if contador == 0:
        numero_max = numero 
        numero_min = numero
    else:
        if numero > numero_max:
            numero_max = numero
        elif numero < numero_min:
            numero_min = numero
    '''
    
    if numero > numero_max or flag_primer_numero == True:
        numero_max = numero
        
    if numero < numero_min or flag_primer_numero == True:
        numero_min = numero
        flag_primer_numero = False
    
    contador += 1
    
print(f'El numero maximo es {numero_max} y el numero minimo es {numero_min}.')

#add flag