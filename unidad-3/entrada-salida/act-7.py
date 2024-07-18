#Maximo Marzetti
'''
Ejercicio 7
Tenemos que obtener el sueldo (por input) que el usuario nos ingrese , transformarlo en
número entero y mostrar el importe de sueldo actualizado con el incremento del 15%
utilizando print.
'''

sueldo = input('Ingrese su sueldo: ')
sueldo = int(sueldo)

actualizacion_sueldo = sueldo + (sueldo * 0.15)
actualizacion_sueldo = int(actualizacion_sueldo )

print(f'Su sueldo es de ${sueldo} con el incremento de 15% queda en ${actualizacion_sueldo}.')