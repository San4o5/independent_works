import mysql.connector
from mysql.connector import Error

def save_employee_to_db(name, salary, days_worked):
    db = None
    try:
        db = mysql.connector.connect(
            host="cont-mysql",
            user="root",
            password="1234",
            database="employee_db"
        )
        cursor = db.cursor()

        query = "INSERT INTO employees (name, salary, days_worked) VALUES (%s, %s, %s)"
        values = (name, salary, days_worked)

        cursor.execute(query, values)
        db.commit()

        print(f"Співробітник {name} доданий до бази даних.")
    except mysql.connector.Error as err:
        print(f"Помилка під час збереження співробітника: {err}")
    finally:
        if db is not None and db.is_connected():
            cursor.close()
            db.close()
