import math

# Ejercicio 5
# Diseñar una función que calcule el área y el perímetro de una circunferencia.

def calculo_area_perimetro(radio):
    return print(f"El area es: {math.pi * radio**2} y el perimetro es: {2 * math.pi * radio}")


calculo_area_perimetro(10)