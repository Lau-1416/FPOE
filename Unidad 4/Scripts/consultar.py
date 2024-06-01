import mysql.connector

def consultar_estudiantes():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='1234567',
        database='universidad'
    )
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM estudiantes')
    estudiantes = cursor.fetchall()
    conn.close()
    return estudiantes

# Ejemplo de uso
estudiantes = consultar_estudiantes()
print("Código | Nombre      | Apellido   | Carrera")
print("---------------------------------------------")
for estudiante in estudiantes:
    print(f"{estudiante[0]:<6} | {estudiante[1]:<10} | {estudiante[2]:<10} | {estudiante[3]}")