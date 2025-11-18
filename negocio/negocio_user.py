from modelos_clases.usuario import Usuario
from prettytable import PrettyTable
from datos import obtener_datos_objetos, modificar_objeto, insertar_objeto, eliminar_objeto
#! from datos import obtener_datos_objetos_deshabilitados, fn_crear_usuario, fn_encriptado_contrasena
from auxiliares import normalizar_cadena
#? from negocio.negocio_email import listado_email
#? from negocio.negocio_posts import listado_posts
#! from iu import ingresar_nombre_marca, ingresar_pais_origen, ingresar_nuevo_nombre_marca

def listado_usuarios():
    tabla_usuarios = PrettyTable()
    tabla_usuarios.field_names = ['ID usuario', 'Nombre usuario']
    listado_usuarios = obtener_datos_objetos(usuario)
    if listado_usuarios:
        for usuario in listado_usuarios:
            tabla_usuarios.add_row(
                [usuario.id, usuario.nombre_usuario])
        print(tabla_usuarios)

def ingresar_nombre_usuario():
    usuario = input('Ingrese nombre de usuario: ')
    for user in obtener_datos_objetos(Usuario):
        if normalizar_cadena(user.nombre_usuario) == normalizar_cadena(usuario):
            return user
    print('Usuario NO existe, verifique el nombre ingresado.')
    return None

def obtener_nombre_usuario(usuario_consultado):
    usuario_encontrado = None
    listado_usuarios = obtener_datos_objetos(Usuario)
    if listado_usuarios:
        for user in listado_usuarios:
            if normalizar_cadena(user.nombre_usuario) == normalizar_cadena(usuario_consultado):
                usuario_encontrado = user
                break
    return usuario_encontrado

def eliminado_logico_user():
    usuario_encontrado = obtener_nombre_usuario()
    if usuario_encontrado:
        usuario_encontrado.habilitado = False
        modificar_objeto()

def eliminado_fisico_user():
    usuario = ingresar_nombre_usuario()
    usuario_encontrado = obtener_nombre_usuario(usuario)
    if usuario_encontrado:
        confirma = input(f'Desea confirmar la eliminación del usuario {usuario_encontrado}? \nESTA ACCION NO SE PUEDE DESHACER\n [presione ENTER para continuar, cualquier otra tecla para cancelar]')
        if confirma == '':
            eliminar_objeto(usuario_encontrado)
            print('Usuario eliminado permanenentemente.')
    else:
        print('Usuario NO existe, vuelva a intentarlo.')

def obtener_hash():
    usuario_encontrado = ingresar_nombre_usuario()
    if usuario_encontrado:
        return usuario_encontrado.pwd
    return None