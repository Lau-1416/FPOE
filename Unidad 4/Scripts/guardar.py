import psycopg2

def insert_student(nombre, apellido, carrera, codigo):
    conn = psycopg2.connect(
        dbname="Universidad",
        user="your_username",
        password="your_password",
        host="localhost"
    )
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO students (nombre, apellido, carrera, codigo)
    VALUES (%s, %s, %s, %s)
    ''', (nombre, apellido, carrera, codigo))
    conn.commit()
    cursor.close()
    conn.close()

#ENSAYO DE GUARDADO
insert_student('Julian', 'Tabares', 'Software', '2156028-2724')