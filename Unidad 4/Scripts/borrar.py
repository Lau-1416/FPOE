import psycopg2

def delete_student(student_id):
    conn = psycopg2.connect(
        dbname="Universidad",
        user="your_username",
        password="your_password",
        host="localhost"
    )
    cursor = conn.cursor()
    cursor.execute('DELETE FROM students WHERE id = %s', (student_id,))
    conn.commit()
    cursor.close()
    conn.close()

# Ejemplo de uso
delete_student(1)