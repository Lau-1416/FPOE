import mysql.connector

def borrar_estudiante(codigo):
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='1234567',
        database='universidad'
    )
    cursor = conn.cursor()
    cursor.execute('DELETE FROM estudiantes WHERE codigo = %s', (codigo,))
    conn.commit()
    conn.close()

# Ejemplo de uso
borrar_estudiante(1)
