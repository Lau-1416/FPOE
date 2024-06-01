import mysql.connector

def crear_tabla():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='1234567',
        database='universidad'
    )
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS estudiantes (
        codigo INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(255) NOT NULL,
        apellido VARCHAR(255) NOT NULL,
        carrera VARCHAR(255) NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

# Ejecutar la función para crear la tabla
crear_tabla()