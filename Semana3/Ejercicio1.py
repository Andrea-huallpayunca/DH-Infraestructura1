# Ejercicio 1
# Crea un programa que pida dos números enteros al usuario y diga si alguno de ellos es múltiplo del otro.
numero1=int(input("Ingresa el primer número: "))
numero2=int(input("Ingresa el segundo número: "))

if numero1 %numero2==0:
  print("El número 1 es múltiplo del 2")
elif numero2 % numero1 ==0 :
  print(f"El numero 2 es multiplo del 1")
else:
  print ("Ningun número es múltiplo del otro")

# resultado ="El numero 1 es multiplo de 2" if numero1 % numero2 ==0 else "El numero 2 es multiplo del 1"
