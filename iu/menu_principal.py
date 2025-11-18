from auxiliares import nombre_aplicacion, numero_version


def menu_pp():
    print(f'{nombre_aplicacion} v.{numero_version}')
    print('=======================================')
    print()
    print('[1] Crear Usuario')
    print('[2] Iniciar Sesión')
    print('[3] Publicar Estado')
    print('[0] Salir')