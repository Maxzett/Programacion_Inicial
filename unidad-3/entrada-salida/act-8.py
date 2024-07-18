#Maximo Marzetti
'''
Ejercicio 8
Tenemos que obtener los valores (por input) que el usuario nos ingrese (sueldo e incremento),
transformarlos en números enteros y mostrar el importe de sueldo actualizado con el
incremento porcentual utilizando print.
'''
sueldo = input('Ingrese su sueldo: ')
sueldo = int(sueldo)

incremento = input('Ingrese su incremento: ')
incremento = int(incremento)

actualizacion_sueldo = sueldo + ((sueldo * incremento)/ 100)
actualizacion_sueldo = int(actualizacion_sueldo)

print(f'Su sueldo es de ${sueldo} con un incremento de %{incremento}, quedaria en ${actualizacion_sueldo}.')