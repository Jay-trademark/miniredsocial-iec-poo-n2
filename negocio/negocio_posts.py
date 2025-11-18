from modelos_clases.post import Post
from modelos_clases.usuario import Usuario
from prettytable import PrettyTable
from datos import obtener_datos_objetos
from datos.conexion import sesion
from .negocio_user import obtener_nombre_usuario

def listado_posts():
    tabla_posts = PrettyTable()
    tabla_posts.field_names = ['ID Post', 'Autor', 'Contenido', 'Likes', 'Fecha']
    listado_posts = obtener_datos_objetos(Post)
    if listado_posts:
        for post in listado_posts:
            nombre_autor = obtener_nombre_usuario(post.autor)
            tabla_posts.add_row(
                [post.id, nombre_autor, post.contenido, post.likes, post.fecha])
        print(tabla_posts)