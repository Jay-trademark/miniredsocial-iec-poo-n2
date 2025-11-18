USE proyecto_poo;

CREATE TABLE IF NOT EXISTS email (
    id INT AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL,    -- max de caracteres es 254
    habilitado TINYINT NOT NULL DEFAULT 1,

    CONSTRAINT pk_email PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT,
    id_email INT NOT NULL,
    nombre_usuario VARCHAR(20) NOT NULL,    -- max de caracteres es 20
    pwd VARCHAR(64) NOT NULL,    -- 63 caracteres en hash
    habilitado TINYINT NOT NULL DEFAULT 1,

    CONSTRAINT pk_usuarios PRIMARY KEY (id)
    CONSTRAINT fk_email_usuario FOREIGN KEY (id_email) REFERENCES email(id)
);

CREATE TABLE IF NOT EXISTS posts (
    id INT AUTO_INCREMENT,
    id_usuario INT NOT NULL,
    contenido VARCHAR(255) NOT NULL,
    fecha_post DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    likes INT NOT NULL DEFAULT 0,
    habilitado TINYINT NOT NULL DEFAULT 1,

    CONSTRAINT pk_posts PRIMARY KEY (id),
    CONSTRAINT fk_usuario_post FOREIGN KEY (id_usuario) REFERENCES usuarios(id)
);

CREATE TABLE IF NOT EXISTS amigos ( 
-- actualmente funciona como seguidores, podria implementarse un sistema de seguimiento mutuo y verificacion de este
    id INT AUTO_INCREMENT,
    id_usuario1 INT NOT NULL,
    id_usuario2 INT NOT NULL,
    habilitado TINYINT NOT NULL DEFAULT 1,

    CONSTRAINT pk_amigos PRIMARY KEY (id)
    CONSTRAINT fk_usuario1_amigo FOREIGN KEY (id_usuario1) REFERENCES usuarios(id),
    CONSTRAINT fk_usuario2_amigo FOREIGN KEY (id_usuario2) REFERENCES usuarios(id)
);