#Maximo Marzetti
'''
Ejercicio 9
Tenemos que crear un programa que deberá obtener el importe que ingrese el usuario por
consola(input), transformar en número y mostrar el importe actualizado con un descuento
del 20% utilizando print.
'''

importe_usuario = input('Ingrese su importe: ')
importe_usuario = int(importe_usuario)

actualizacion_importe = importe_usuario - (importe_usuario  * 0.20)
actualizacion_importe = int(actualizacion_importe )

print(f'Su importe es de ${importe_usuario} con el descuento del 20% queda en ${actualizacion_importe}.')