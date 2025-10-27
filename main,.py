from iu.menu_principal import menu_principal


def main():
    while True:
        print()
        menu_principal()
        print()
        opcion = input("Seleccione su opción [0-3]: ")

        if opcion == "1":
            pass
        elif opcion == "2":
            pass
        elif opcion == "3":
            pass
        elif opcion == "0":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción NO corresponde, ingrese nuevamente...")


main()
