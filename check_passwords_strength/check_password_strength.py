# check_password_strength.py
# Script básico para comprobar la fortaleza de una contraseña
# Hecho para ayudar a entender qué hace que una contraseña sea débil o fuerte.

def es_fuerte(password):
    """
    Comprueba si una contraseña es fuerte.
    Una contraseña se considera fuerte si:
    - Tiene al menos 8 caracteres.
    - Contiene al menos una letra mayúscula.
    - Contiene al menos una letra minúscula.
    - Contiene al menos un dígito.
    - Contiene al menos un carácter especiales
    """
    if len(password) < 8:
        return False
    
    tiene_mayus = any(c.isupper() for c in password)
    tiene_minus = any(c.islower() for c in password)
    tiene_num = any(c.isdigit() for c in password)
    simbolos = "!@#$%^&*()-_=+[]{\}|;:'~,.<>?/"
    tiene_simbolos = any(c in simbolos for c in password)

    return tiene_mayus and tiene_minus and tiene_num and tiene_simbolos

def main():
    print("Comprobador básico de fuerza de contraseñas")
    passwd = input("Introduce ña contraseña a comprobar: ")

    if es_fuerte(passwd):
        print("La contraseña parece fuerte. ")
    else:
        print("La contraseña es débil. Intenta usar una combinación de mayúsculas, minúsculas, números y símbolos, y que tenga al menos 8 caracteres. ")
        if __name__ == "__main__":
            main()