import time
import psycopg2
from psycopg2 import OperationalError

while True:
    try:
        conn = psycopg2.connect(
            dbname="cinema",
            user="postgres",
            password="postgres",
            host="db",
            port="5432"
        )
        conn.close()
        break
    except OperationalError:
        print("Database unavailable, waiting 1 second...")
        time.sleep(1)

print("Database available!")
