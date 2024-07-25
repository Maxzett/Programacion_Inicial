# Maximo Marzetti
"""
La juguetería El MUNDO DE CHARLY nos encarga un programa para conocer qué cantidad de materiales se necesita para la fabricación de distintos juguetes.

CONFECCIÓN DE UN COMETA:
https://www.utnfravirtual.org.ar/pluginfile.php/561436/mod_assign/intro/cometade.png
Medidas:
AB = Diágonal mayor
DC = Diágonal menor
BD y BC = lados menores
AD y AC = lados mayores

El usuario ingresará las medidas  BC, CD y DA.

Detalles de construcción

Debemos tener en cuenta que la estructura del cometa estará dada por un perímetro de varillas de plástico y los correspondientes entrecruces (DC y AB) del mismo material para mantener la forma del cometa.

El cometa estará construido con papel de alta resistencia. La cola del mismo se construirá con el mismo papel que el cuerpo y representará un 10% adicional del necesario para el cuerpo.

Necesitamos saber cuántos Mts de varillas de plástico y cuántos de papel son necesarios para la construcción en masa de 10 cometas. Tener en cuenta que los valores de entrada están expresados en Cms.
"""

BC = float(input("Ingrese la medida BC (en Cms): "))
CD = float(input("Ingrese la medida CD (en Cms): "))
DA = float(input("Ingrese la medida DA (en Cms): "))

BC = BC / 100
CD = CD / 100
DA = DA / 100

#diagonal mayor
AB = (DA + BC) - CD
#varillas cometa
perimetro = BC * 2 + DA * 2 + CD + AB
#papel cometa
area_cometa = (AB * CD) / 2
cola = 1.10
papel_cometa = area_cometa * cola
#total varillas necesarias
total_varillas = perimetro * 10
#total papel necesario
total_papel = papel_cometa * 10

print(f'El total de varillas necesarias es de {total_varillas:.2f}mts y el total de papel necesario es de {total_papel:.2f}mts cuadrados.')