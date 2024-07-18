#Maximo Marzetti
'''
Agencia de viaje:
Para saber el costo de un viaje necesitamos el siguiente algoritmo, sabiendo que el precio por
kilo de pasajero es 1000 pesos.Se ingresan todos los datos por PROMPT los datos a solicitar
de dos personas son: nombre, edad y peso
Se pide armar el siguiente mensaje:
"Hola jose y maria , sus pesos son 80 kilos y 60 kilos respectivamente, sumados da 140 kilos ,
el promedio de edad es 33 y su viaje vale 140000 pesos "
'''

p1_nombre = input('Nombre primer persona: ')
p1_edad = input('Edad primer persona: ') 
p1_edad = int(p1_edad)
p1_peso = input('Peso primer persona: ')
p1_peso = int(p1_peso)

p2_nombre = input('Nombre segunda persona: ')
p2_edad = input('Edad segunda persona: ') 
p2_edad = int(p2_edad)
p2_peso = input('Peso segunda persona: ')
p2_peso = int(p2_peso)

precio_kilo_pasajero = 1000
suma_pesos = p1_peso + p2_peso
promedio_edad = (p1_edad + p2_edad)//2
valor_viaje = precio_kilo_pasajero * suma_pesos

print(f'Hola {p1_nombre} y {p2_nombre}, sus pesos son {p1_peso} kilos y {p2_peso} kilos respectivamente, sumados da {suma_pesos} kilos, el promedio de edad es {promedio_edad} y su viaje vale {valor_viaje} pesos.')