from auxiliares.info_aplicacion import nombre_aplicacion
from auxiliares.version import numero_version


def menu_principal():
    print(f"{nombre_aplicacion} v.{numero_version}")
    print("=======================================")
    print("[1] Gestión  Empleados")
    print("[2] Gestión  Proyectos")
    print("[3] Gestión  Horarios")
    print("[0] Salir")
