'''
Maximo Marzetti
Ejercicio 7
Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). Calcular la suma de los números positivos y el producto de los negativos.
'''
acumulador_positivos = 0
acumulador_negativos = 1
contador_negativos = 0

while True:
    numero = int(input('Ingrese un numero positivo o negativo: '))
    if numero > 0:
        acumulador_positivos += numero
    elif numero < 0:
        acumulador_negativos = acumulador_negativos * numero
        contador_negativos += 1
    
    respuesta = input('Continuar ingresando numeros ? (ingrese "no" para salir)  ')
    if respuesta == 'no':
        break
if contador_negativos == 0:
    acumulador_negativos = 0
    
print(f'''
      Suma positivos: {acumulador_positivos}
      Producto de los negativos: {acumulador_negativos}
      ''')