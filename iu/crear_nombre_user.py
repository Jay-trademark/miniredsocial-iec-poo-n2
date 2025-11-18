def crear_nombre_usuario():
    loop = True
    while loop:
        username = input("Utilice solo letras, numeros y/o guiones bajos \nIngrese un nombre de usuario: ").strip()
        if len(username) > 20:
            print("El nombre de usuario es muy largo. Use un maximo de 20 caracteres.")
        else:
            val_char = True
            for char in username:
                if not (char.isalnum() or char == '_'):
                    print("Nombre de usuario inválido. Utilice solo letras, numeros y/o guiones bajos.")
                    val_char = False
            if val_char:
                loop = False
                return username