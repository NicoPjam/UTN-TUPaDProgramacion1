
import psycopg2
from Clases import *

DB_CONFIG = {
    'dbname': "Biblioteca",
    'user': "postgres",
    'password': "A#p0ST5921",
    'host': "localhost",
    'port': "5432"
}

def inicializar_base_datos():
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS autores (
                    id SERIAL PRIMARY KEY,
                    nombre VARCHAR(100) NOT NULL,
                    nacionalidad VARCHAR(50) NOT NULL
                );
            """)
            cur.execute("""
                CREATE TABLE IF NOT EXISTS libros (
                    id SERIAL PRIMARY KEY,
                    titulo VARCHAR(200) NOT NULL,
                    anio INT NOT NULL,
                    autor_id INT REFERENCES autores(id)
                );
            """)
        conn.commit()

def registrar_autor(nombre: str, nacionalidad: str):
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO autores (nombre, nacionalidad) VALUES (%s, %s) RETURNING id;", (nombre, nacionalidad))
            autor_id = cur.fetchone()[0]
        conn.commit()
    return autor_id
def registrar_libro(titulo: str, anio: int, autor_id: int):
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO libros (titulo, anio, autor_id) VALUES (%s, %s, %s) RETURNING id;", (titulo, anio, autor_id))
            libro_id = cur.fetchone()[0]
        conn.commit()
    return libro_id

def listar_libros():
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT l.id, l.titulo, l.anio, a.id, a.nombre, a.nacionalidad
                FROM libros l
                JOIN autores a ON l.autor_id = a.id;
            """)
            libros = []
            for row in cur.fetchall():
                autor = Autor(row[3], row[4], row[5])
                libro = Libro(row[0], row[1], row[2], autor)
                libros.append(libro)
        return libros
def actualizar_libro(libro_id: int, nuevo_titulo: str, nuevo_anio: int, nuevo_autor_id: int):
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute("UPDATE libros SET titulo = %s, anio = %s, autor_id = %s WHERE id = %s;", (nuevo_titulo, nuevo_anio, nuevo_autor_id, libro_id))
        conn.commit()
def eliminar_libro(libro_id: int):
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM libros WHERE id = %s;", (libro_id,))
        conn.commit()

if __name__ == "__main__":
    inicializar_base_datos()
    # Ejemplo de uso
    autor_1 = registrar_autor("Gabriel García Márquez", "Colombiana")
    autor_2 = registrar_autor("Isabel Allende", "Chilena")
    libro_1 = registrar_libro("Cien Años de Soledad", 1967, autor_1)
    libro_2 = registrar_libro("El Amor en los Tiempos del Cólera", 1985, autor_1)
    libro_3 = registrar_libro("Crónica de una Muerte Anunciada", 1981, autor_1)
    libro_4 = registrar_libro("Cien Años de Soledad (Edición Especial)", 1967, autor_1)
    libro_5 = registrar_libro("La Casa de los Espíritus", 1982, autor_2)
    libros = listar_libros()
    for libro in libros:
        print(libro)
    actualizar_libro(libro_1, "Cien Años de Soledad (Edición Especial)", 1967, autor_1)
    eliminar_libro(libro_3)