import psycopg2

def crearTabla():
    # Conexión a la base de datos
    conn = psycopg2.connect(
        dbname="universidad",
        user="ame",
        password="1234567",
        host="localhost"
    )
    cursor = conn.cursor()

    # Crear la tabla
    cursor.execute('''
    CREATE TABLE students (
        id SERIAL PRIMARY KEY,
        nombre VARCHAR(100) NOT NULL,
        apellido VARCHAR(100) NOT NULL,
        carrera VARCHAR(100) NOT NULL,
        codigo VARCHAR(50) NOT NULL
    )
    ''')

    #Confirmar la transacción
    conn.commit()

    #Cerrar la conexión
    cursor.close()
    conn.close()

#Ejecutar el script
crearTabla()