def fn_crear_usuario(user):
    loop = True
    while loop:
        username = input("Solo utilice letras, numeros y/o guiones bajos \nIngrese un nombre de usuario: ").strip()
        for char in username:
            if not (char.isalnum() or char == '_'):
                print("Nombre de usuario inválido. Utilice solo letras, numeros y/o guiones bajos.")
            elif len(username) > 20:
                    print("El nombre de usuario es muy largo. Use un maximo de 20 caracteres.")
            else:
                loop = False
                return username