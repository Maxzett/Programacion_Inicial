#Maximo Marzetti
'''
Permitir que el usuario ingrese todos los números que desee. Determinar:
La suma acumulada de los números negativos.
La suma acumulada de los números positivos.
La cantidad de números negativos ingresados.
El promedio de los números positivos.
El porcentaje de números negativos ingresados, respecto del total de ingresos.
'''
suma_negativos = 0
suma_positivos = 0
cant_negativos = 0
cant_positivos = 0
total_ingresos = 0

while True:
    num = input('Ingrese un numero: ')
    num = int(num)
    if num < 0:
        cant_negativos += 1
        suma_negativos += num 
    else:
        cant_positivos += 1
        suma_positivos += num
    
    total_ingresos += 1
    
    respuesta = input('Continuar ingresando numeros ? (ingrese "no" para salir)  ')
    if respuesta == 'no':
        break
    
promedio_positivos = suma_positivos / cant_positivos
porcentaje_negativos = (cant_negativos / total_ingresos) * 100 

print(f'''
La suma de numeros negativos es: {suma_negativos}
La suma de numeros positivos es: {suma_positivos}
La cantidad de numeros negativos ingresados es: {cant_negativos}
El promedio de numeros positivos es: {promedio_positivos}
El porcentaje de numeros negativos ingresados, respecto al total es: {porcentaje_negativos}%
{total_ingresos}
''')