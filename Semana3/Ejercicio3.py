from Ejercicio2 import temperaturaMedia
# Ejercicio 3
# Crear un programa principal, que utilizando la función anterior, vaya pidiendo la temperatura máxima y mínima de cada día y vaya mostrando la media. El programa pedirá el número de días que se van a introducir.

numerodias = int(input("Ingrese el número de días a evaluar: "))
temperaturaMinima=int(input("Ingrese la temperatura mínima: "))
temperaturaMaxima=int(input("Ingrese la temperatura máxima: "))

temperaturaM= temperaturaMedia(temperaturaMaxima,temperaturaMinima)
print(f"La temperatura media es {temperaturaM} C°")
