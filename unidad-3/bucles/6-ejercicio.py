'''
Maximo Marzetti
Ejercicio 6
Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). Calcular la suma de los números ingresados y el promedio de los mismos.
'''
suma = 0
numeros = int(input("Introduce un número o escribe 0 para detener: "))

while numeros != 0:
    suma += numeros
    numeros = int(input("Introduce un número o escribe 0 para detener: "))
    
promedio = suma / numeros
    
print(f'Suma: {suma}')
print(f'Promedio: {promedio}')
