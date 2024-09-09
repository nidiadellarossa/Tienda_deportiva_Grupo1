import time
import json
import re
def credentials_validator(username, password):
    
    if len(username) < 8:
        print("El nombre de usuario debe tener al menos 8 caracteres.")
        return False

    if len(password) < 8:
        print("La contraseña debe tener al menos 8 caracteres.")
        return False

    # Validar condiciones adicionales de la contraseña
    met_conditions = 0

    # i. al menos 1 minúscula
    if re.search(r"[a-z]", password):
        met_conditions += 1

    # ii. al menos 1 mayúscula
    if re.search(r"[A-Z]", password):
        met_conditions += 1

    # iii. al menos 1 número
    if re.search(r"\d", password):
        met_conditions += 1

    # iv. al menos un caracter especial
    if re.search(r"\W", password):
        met_conditions += 1

    if met_conditions < 2:
        print("La contraseña debe cumplir con al menos dos de las condiciones adicionales.")
        return False

    return True
def user_registration(username, password):
    try:
        with open('user_data.json', 'r') as file:
            users = json.load(file)
    except FileNotFoundError:
        users = {}

    if username in users:
        print("El usuario ya existe.")
        return False

    users[username] = {
        "password": password,
        "invalid_login": 0
    }

    print("USER")

    with open('user_data.json', 'w') as file:
        json.dump(users, file)
    print("Usuario registrado exitosamente.")

    return True

def user_login(username, password):
    try:
        with open('user_data.json', 'r') as file:
            users = json.load(file)
    except FileNotFoundError:
        print("Usuario no encontrado.")
        time.sleep(3)
        return False

    if username not in users:
        print("Usuario no encontrado.")
        time.sleep(3)
        return False

    if users[username]["invalid_login"] >= 4:
        print("Cuenta bloqueada por seguridad.")
        time.sleep(3)
        return False

    if users[username]["password"] != password:
        print("Password incorrecto.")
        users[username]["invalid_login"] += 1
        print(f'Intentos de ingreso invalidos: {users[username]["invalid_login"]}')
        print('Importante: Al cuarto intento fallido la cuenta se bloquea por razones de seguridad')
        with open('user_data.json', 'w') as file:
            json.dump(users, file)
        time.sleep(3)
        return False

    return True