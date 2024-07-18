#Maximo Marzetti
'''
Ejercicio 10
Tenemos que crear un programa que deberán obtener el importe y el descuento que ingrese el
usuario por consola, transformarlos en números y mostrar el importe actualizado con el
descuento utilizando print.
'''
importe = input('Ingrese su importe: ')
importe = int(importe)

descuento = input('Ingrese su descuento: ')
descuento = int(descuento)

actualizacion_importe = importe - ((importe * descuento)/ 100)
actualizacion_importe = int(actualizacion_importe)

print(f'Su importe es de ${importe} con un descuento de %{descuento}, quedaria en ${actualizacion_importe}.')