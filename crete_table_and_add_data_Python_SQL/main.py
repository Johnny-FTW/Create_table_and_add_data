import psycopg2
import os

def print_menu():
    print("\n----------------------------")
    print("WELCOME")
    print("Menu options:")
    print("\t[0] to insert a employee")
    print("\t[1] to terminate")

def create_employee():
    print("Employee details:")
    while True:
        try:
            name=input("Name: ")
            surname=input("Surname: ")
            insert_to_sql(name,surname)
        except Exception as e:
            print(e)
            print("Error during employee creation please renter details")
            continue
        break


def insert_to_sql(name, surname):
    conn = psycopg2.connect(
        host=os.getenv("POSTGRES_HOST", "localhost"),
        database=os.getenv("DATABASE", "postgres"),
        user=os.getenv("POSTGRES_USER", "postgres"),
        password=os.getenv("POSTGRES_PASSWORD", "postgres")
    )
    with conn, conn.cursor() as cur:
            cur.execute(f"INSERT INTO employee (name, surname) VALUES ('{name}', '{surname}');")
    conn.close()


if __name__ == "__main__":
    while True:

        while True:
            try:
                print_menu()
                menu_choice=int(input("Menu choice: "))
                if menu_choice<0 or menu_choice >=2:
                    raise Exception("Wrong menu choice")
                break
            except Exception as e:
                print(e)
                print("Please choose valid menu choice")

        if menu_choice == 1:
            print("Bye!!")
            break
        if menu_choice == 0:
            create_employee()