from modelos_clases.email import Email
from prettytable import PrettyTable
from datos import obtener_datos_objetos

def listado_email():
    tabla_email = PrettyTable()
    tabla_email.field_names = ['ID email', 'E-Mail']
    listado_email = obtener_datos_objetos(Email)
    if listado_email:
        for email in listado_email:
            tabla_email.add_row(
                [email.id, email.nombre_usuario])
        print(tabla_email)