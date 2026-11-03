import psycopg

conn = psycopg.connect(
    user="postgres",
    password="Habhi@123",
    host="localhost",
    port=5432,
    dbname="postgres",
    autocommit=True
)

cur = conn.cursor()
cur.execute("SELECT datname FROM pg_database WHERE datname LIKE '%Clinic%';")
print("Found databases:", cur.fetchall())

try:
    cur.execute('ALTER DATABASE "ClinicRIse " RENAME TO clinicrise;')
    print("Successfully renamed 'ClinicRIse ' to 'clinicrise'!")
except Exception as e:
    print("Error renaming:", e)

cur.execute("SELECT datname FROM pg_database WHERE datname LIKE '%clinic%';")
print("Current databases:", cur.fetchall())
conn.close()

