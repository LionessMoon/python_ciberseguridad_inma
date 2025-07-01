# crack_passwords.py
# Script básico para demostrar cracking de contraseñas con fuerza bruta.

def brute_force_password(password,charset):
    attempts = 0
    for char in charset:
        attempts += 1
        if chaar == password:
            print(f"Contraseña encontrada: {char} en {attempts} intentos.")
            return True
        print("Contraseña no encontrada en los caracteres probados.")
        return False
if __name__ == "__main__":
    password_to_crack = input("Introduce la contraseña (un solo carácter para esta demo):")
    charset = "abcdefghijklmnñopqrstuvwxyz0123456789"

    brute_force_password(password_to_crack, charset)        