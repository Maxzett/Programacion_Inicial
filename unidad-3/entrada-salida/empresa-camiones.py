#Maximo Marzetti
'''
Empresa de Camiones:
Para el departamento de logística:
A. Es necesario saber la cantidad de camiones que harían falta para transportar los
materiales que se utilizarán para la construcción de un edificio. Para ello, se ingresa la
cantidad de toneladas necesarias de materiales a transportar. El programa deberá
informar la cantidad de camiones, sabiendo que cada uno de ellos puede transportar por
viaje 3500kg.
B. A partir del ingreso de la cantidad de kilómetros que tiene que recorrer estos camiones
para llegar al destino de la obra, necesitamos que el programa informe cual es el tiempo
(en horas) que tardará cada uno de los camiones, si sabemos que cada camión puede ir
a una velocidad máxima y constante de 90 km/h.
'''

materiales_necesarios = input('Cantidad de toneladas necesarias de materiales a transportar: ')
materiales_necesarios = float(materiales_necesarios)

max_peso_camiones = 3.5
cantidad_camiones = (materiales_necesarios/max_peso_camiones) + 1
cantidad_camiones = int(cantidad_camiones)

print(f'Vas a necesitar {cantidad_camiones} camiones ')

kilometros_a_recorrer = input('Cantidad de kilometros a recorrer hasta la obra: ')
kilometros_a_recorrer = float(kilometros_a_recorrer)

velocidad_max_camiones = 90

horas_viaje = kilometros_a_recorrer / velocidad_max_camiones

print(f'Van a tardar {horas_viaje:.2f} horas para llegar a la obra')