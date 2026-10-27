import os
import time
import pandas as pd
import psycopg2

# Dataset de ejemplo para demostrar el flujo ETL del laboratorio.
datos = pd.DataFrame([
    {'id': 1, 'nombre': 'Ana', 'ciudad': 'Lima'},
    {'id': 2, 'nombre': 'Luis', 'ciudad': 'Arequipa'},
    {'id': 3, 'nombre': 'Rosa', 'ciudad': 'Cusco'},
])
datos['nombre'] = datos['nombre'].str.strip()

for intento in range(10):
    try:
        conexion = psycopg2.connect(
            host=os.getenv('DB_HOST', 'localhost'),
            port=os.getenv('DB_PORT', '5432'),
            dbname=os.getenv('DB_NAME', 'laboratorio'),
            user=os.getenv('DB_USER', 'admin'),
            password=os.getenv('DB_PASSWORD', 'admin123'),
        )
        break
    except psycopg2.OperationalError:
        if intento == 9:
            raise
        time.sleep(2)

with conexion:
    with conexion.cursor() as cursor:
        cursor.execute('CREATE TABLE IF NOT EXISTS clientes (id INTEGER PRIMARY KEY, nombre TEXT NOT NULL, ciudad TEXT NOT NULL)')
        for fila in datos.itertuples(index=False):
            cursor.execute('INSERT INTO clientes (id, nombre, ciudad) VALUES (%s,%s,%s) ON CONFLICT (id) DO UPDATE SET nombre=EXCLUDED.nombre, ciudad=EXCLUDED.ciudad', (fila.id, fila.nombre, fila.ciudad))
        cursor.execute('SELECT COUNT(*) FROM clientes')
        total = cursor.fetchone()[0]
        print(f'Procesamiento terminado. Registros en clientes: {total}')
conexion.close()
