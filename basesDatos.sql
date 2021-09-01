CREATE DATABASE IF NOT EXISTS mi_base;
use mi_base;         /* aqui hay qu especificar que base voy  usar*/

CREATE TABLE usuarios(
id         int(25) auto_increment not null,
nombre     varchar(100),
apellidos  varchar(255),
email      varchar(255) not null,
password   varchar(255) not null,
fecha      date not null,
CONSTRAINT pk_usuarios PRIMARY KEY(id),  /* aqui le dije que el id va aser la calve primaria() */
CONSTRAINT uq_email UNIQUE(email)  /* campo unico  queno puede ver dos */
)ENGINE=InnoDb;  /* PARA MANTENER RELACIONES CON OTRAR TABLAS */


CREATE TABLE notas(
id             int(25) auto_increment not null,
usuario_id     int(25) not null,                   /* (usuario_id)columna para relacionar esta tabla con la tabla de usuario */
titulo         varchar(255) not null,            /* para saber que nota s de cada usuario (le puede poner cual quier nombre)*/
descripcion  MEDIUMTEXT,
fecha          date not null,
CONSTRAINT  pk_notas PRIMARY KEY(id), /*Cla ve primariaa de esta tabla*/
CONSTRAINT  fk_nota_usuario FOREIGN KEY(usuario_id) REFERENCES usuarios(id) /* aqui le dije que relacione el campo(usuario_id) con latabla(usuario(id))*/
)ENGINE=InnoDb;                                              

