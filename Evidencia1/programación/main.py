import os
import time
from modules.admin_menu import admin_menu
from modules.user_utilities import credentials_validator, user_registration, user_login
from modules.captcha import generate_captcha

clear_command = 'cls' if os.name == 'nt' else 'clear'

while True:
    print("Bienvenidos a la aplicación StoreManager V1.0 \n")
    print("1. Ingresar a la aplicación")
    print("2. Registrar usuario")
    print("3. Salir")

    user_choice = input("Ingrese su opción: ")

    if user_choice == "1":
        os.system(clear_command)
        print("INGRESAR CREDENCIALES \n")
        # Ingresar a la aplicación
        username = input("Ingrese su nombre de usuario: ")
        password = input("Ingrese su contraseña: ")

        if user_login(username, password):
                admin_menu()
        os.system(clear_command)    
    elif user_choice == "2":
        os.system(clear_command)
        print("REGISTRAR NUEVO USUARIO \n")
        # Registrar usuario
        username = input("Ingrese su nombre de usuario: ")
        password = input("Ingrese su contraseña: ")

        if credentials_validator(username, password):
            operando, resultado = generate_captcha()
            print(f"Captcha: {operando}")
            user_captcha = input("Ingrese el resultado del captcha: ")
            print(f"Captcha: {resultado}")
            if user_captcha == str(resultado):
                print("ENTO AL CATCH")
                user_registration(username, password)
                print("USUARIO CREADO!")
                time.sleep(3)
                os.system(clear_command)
            else:
                print("ERROR EN EL CAPTCHA.")
                os.system(clear_command)
        else:
            print("Error al registrar el usuario.")
        time.sleep(3)
        os.system(clear_command)
    elif user_choice == "3":
        os.system(clear_command)
        print("Saliendo de la aplicación...")
        time.sleep(1)
        break
    else:
        os.system(clear_command)
        print("Opción no válida, vuelva a intentar...")
        time.sleep(1)
        os.system(clear_command)
