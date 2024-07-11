print(
"""
+================================+
| ¡Bienvenido a mi juego, Junior!|
| Introduce un número entero |
| y adivina qué número he |
| elegido para ti. |
+================================+
""")

num_secreto = 6
num_usuario = int(input('¿Cuál es el número secreto?  ')) 

while num_usuario != num_secreto:
    if num_usuario != num_secreto:
        print('¡Ja, ja! ¡Estás atrapado en mi bucle!')
    num_usuario = int(input('Vuelve a intentarlo:  '))
print('¡Bien hecho, Junior! Eres libre ahora.')