import mysql.connector

def actualizar_estudiante(codigo, nombre, apellido, carrera):
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='1234567',
        database='universidad'
    )
    cursor = conn.cursor()
    cursor.execute('''
    UPDATE estudiantes
    SET nombre = %s, apellido = %s, carrera = %s
    WHERE codigo = %s
    ''', (nombre, apellido, carrera, codigo))
    conn.commit()
    conn.close()

# Ejemplo de uso
actualizar_estudiante(1, 'Juan', 'Gomez', 'Arquitectura')
