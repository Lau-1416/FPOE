import mysql.connector

def insertar_estudiante(nombre, apellido, carrera):
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='password',
        database='universidad'
    )
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO estudiantes (nombre, apellido, carrera)
    VALUES (%s, %s, %s)
    ''', (nombre, apellido, carrera))
    conn.commit()
    conn.close()

# Ejemplo de uso
insertar_estudiante('Juan', 'Perez', 'Ingenieria')