'''
Maximo Marzetti
Ejercicio 4
Mostrar la suma de los números pares desde el 1 hasta el 10.
'''

contador = 0 
suma_pares = 0

while contador < 10:
    contador += 2
    suma_pares += contador
    
print(suma_pares)