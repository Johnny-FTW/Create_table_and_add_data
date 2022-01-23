import os
import psycopg2

from psycopg2 import sql

if __name__ == "__main__":
    conn=psycopg2.connect(
        host=os.getenv("POSTGRES_HOST", "localhost"),
        database=os.getenv("POSTGRES_DATABASE", "postgres"),
        user=os.getenv("POSTGRES_USER", "postgres"),
        password=os.getenv("POSTGRES_PASSWORD", "postgres"),
    )
    print("CONNECTED TO SQL")
    with conn, conn.cursor() as cur:
        create_employee_table_query=sql.SQL(
            """
            DROP TABLE IF EXISTS employee;
            CREATE TABLE employee (
                employe_id SERIAL PRIMARY KEY,
                name VARCHAR(128),
                surname VARCHAR(128) 
            );
            """
        )
        print(create_employee_table_query.as_string(cur))
        cur.execute(create_employee_table_query)
    conn.close()
    print("TABLE WAS CREATED")