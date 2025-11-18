import pwinput
import bcrypt

def encriptado_contrasena(contra: str):
    hashed = bcrypt.hashpw(contra.encode(), bcrypt.gensalt())
    return hashed.decode()

def confirmar_contrasena():
    loop = True
    while loop:
        contra = pwinput.pwinput(prompt="Ingrese contraseña: ", mask="*")
        contra2 = pwinput.pwinput(prompt="Repita contraseña: ", mask="*")
        if contra == contra2:
            loop = False
            return encriptado_contrasena(contra)
        else:
            print("Las contraseñas no coinciden. Intente nuevamente.")

def check_password(plain: str, hashed: str) -> bool:
    try:
        return bcrypt.checkpw(plain.encode(), hashed.encode())
    except Exception:
        return False
