#Maximo Marzetti
'''
Ferrete Lámparas

En una ferretería se quiere implementar un sistema que permita a los usuarios saber cuánto deberán pagar por la compra de lámparas de bajo consumo. Se tiene en cuenta que todas las lámparas cuestan $800.
A partir de la cantidad y marca de las lámparas compradas (solo se puede comprar una marca por vez) se aplicará el siguiente descuento:
Si compra 6 o más  lámparas bajo consumo tiene un descuento del 50%. 
Si compra 5  lámparas bajo consumo marca "ArgentinaLuz" se hace un descuento del 40 % y si es de otra marca el descuento es del 30%.
Si compra 4  lámparas bajo consumo marca "ArgentinaLuz" o “FelipeLamparas” se hace un descuento del 25 % y si es de otra marca el descuento es del 20%.
Si compra 3  lámparas bajo consumo marca "ArgentinaLuz"  el descuento es del 15%, si es  “FelipeLamparas” se hace un descuento del 10 % y si es de otra marca un 5%.
Por otro lado, si el importe final con descuento suma más de $4000  se obtiene un descuento adicional de 5%.
Mostrar por pantalla: 
Marca, cantidad de lámparas, total a pagar sin descuento, el descuento obtenido si corresponde, el descuento adicional (si corresponde) y el total a pagar con descuento.
'''

lamparas_usuario = int(input('Cantidad de lamparas a comprar: '))
marcas = input('Elija la marca de su lampara: ArgentinaLuz / FelipeLamparas / Generica. ')

lampara = 800
descuento = 0
importe_descuento_adicional = 4000
precio_final = 0

if lamparas_usuario >= 6: 
    porcentaje_descuento = 0.50
elif lamparas_usuario == 5:
    if marcas == 'ArgentinaLuz':
        porcentaje_descuento = 0.40
    else:
        porcentaje_descuento = 0.30
elif lamparas_usuario == 4:
    if marcas == 'ArgentinaLuz' or 'FelipeLamparas':
        porcentaje_descuento = 0.25
    else:
        porcentaje_descuento = 0.20      
elif lamparas_usuario == 3:
    if marcas == 'ArgentinaLuz':
        porcentaje_descuento = 0.15
    elif marcas == 'FelipeLamparas':
        porcentaje_descuento = 0.10
    else:
        porcentaje_descuento = 0.05
    
precio_sin_descuento = lamparas_usuario * lampara
descuento = precio_sin_descuento * porcentaje_descuento
descuento = int(descuento)
precio_con_descuento = precio_sin_descuento - descuento

if precio_con_descuento >= importe_descuento_adicional:
    porcentaje_descuento = 0.05
    descuento_extra = precio_con_descuento * porcentaje_descuento
    precio_final = precio_con_descuento - descuento_extra
else:
    precio_final = precio_con_descuento

precio_final = int(precio_final)

print(f'Su cantidad de lamparas es {lamparas_usuario}, el valor a pagar es de ${precio_sin_descuento}, con su descuento de ${descuento}, el precio final seria de ${precio_final}.')