import psycopg2

def update_student(student_id, nombre, apellido, carrera, codigo):
    conn = psycopg2.connect(
        dbname="Universidad",
        user="your_username",
        password="your_password",
        host="localhost"
    )
    cursor = conn.cursor()
    cursor.execute('''
    UPDATE students
    SET nombre = %s, apellido = %s, carrera = %s, codigo = %s
    WHERE id = %s
    ''', (nombre, apellido, carrera, codigo, student_id))
    conn.commit()
    cursor.close()
    conn.close()

# Ejemplo de uso
update_student(1, 'Maria', 'Lopez', 'Medicina', '54321')