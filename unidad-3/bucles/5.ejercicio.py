'''
Maximo Marzetti
Ejercicio 5
Solicitar el ingreso de 5 números, calcular la suma de los números ingresados y el promedio. Mostrar por pantalla.
'''
contador = 0 
suma = 0

while contador < 5:
    numeros = int(input('Ingrese un numero: '))
    suma += numeros
    contador += 1
promedio = suma / contador
    
print(f'Suma: {suma}')
print(f'Promedio: {promedio}')
