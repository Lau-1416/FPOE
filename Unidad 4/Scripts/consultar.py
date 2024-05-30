import psycopg2

def get_students():
    conn = psycopg2.connect(
        dbname="Universidad",
        user="your_username",
        password="your_password",
        host="localhost"
    )
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM students')
    students = cursor.fetchall()
    cursor.close()
    conn.close()
    return students

# Ejemplo de uso
students = get_students()
for student in students:
    print(student)