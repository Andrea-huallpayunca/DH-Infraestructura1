# Ejercicio 7
# Crear un programa principal donde se pida un nombre de usuario y una contraseña y se intente hacer login. El usuario tendrá únicamente tres oportunidades para intentarlo.

from Ejercicio6 import Login


def main():
    intentos = 3
    while intentos > 0:
        user = input("Ingresa tu usuario: ")
        password = input("Ingresa tu contrasena: ")
        if Login(user, password):
            return print(f"Login correcto. Bienvenido {user}!")
            
        else:
            intentos -= 1
            print(f"Login incorrecto, te quedan {intentos} intentos.")

    return print(f"Has agotado todos tus intentos, acceso denegado.")

main()