import psycopg
import pandas as pd
import os

connection = psycopg.connect(
    host="localhost",
    port="5432",
    user="postgres",
    password="Datacraft",
    dbname="musikdaten"
)
cursor = connection.cursor()

output_folder = r'C:\Users\Admin\Documents\Projektwoche_SQL\Projektwoche_SQL\src\database'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

cursor.execute("""
    SELECT table_name
    FROM information_schema.tables
    WHERE table_schema = 'public'
""")
tables = cursor.fetchall()

for table in tables:
    table_name = table[0]

    query = f'SELECT * FROM {table_name}'
    df = pd.read_sql(query, connection)

    csv_file = os.path.join(output_folder, f'{table_name}.csv')
    df.to_csv(csv_file, index=False)
    print(f'Tabelle {table_name} wurde als {csv_file} gespeichert.')

cursor.close()
connection.close()
