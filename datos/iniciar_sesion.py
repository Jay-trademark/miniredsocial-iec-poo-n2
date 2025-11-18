from ..auxiliares.encriptado_contra import check_password
import pwinput
from ..negocio.negocio_user import obtener_nombre_usuario

def login():
    user = input("Usuario: ")
    usuario = obtener_nombre_usuario(user)
    if usuario:
        contra = pwinput.pwinput(prompt="Ingrese contraseña: ", mask="*")
        if check_password(contra, usuario.pwd):
            print("\nAcceso concedido.")
        else:
            print("\nAcceso denegado.")
    else:
        print("\nUsuario no encontrado.")