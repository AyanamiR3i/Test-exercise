from flask import Flask, render_template
from flask_mysqldb import MySQL
from mysql.connector import connect, Error

app = Flask(__name__)

try:
    with connect(
            host="localhost",
            user=input("Введите имя пользователя: "),
            password="",
            database="db_students"
    ) as connection:
        show_db_query = "SHOW DATABASES"
        with connection.cursor() as cursor:
            cursor.execute(show_db_query)
            for db in cursor:
                print(db)

except Error as e:
    print(e)

mysql = MySQL(app)


def main():
    print("Выберите таблицу для редактирования:\n1. Студенты\n2. Группы\n3. Предметы\n4. Оценки")
    choose = (int)(input("Выбор:"))
    print(choose)
    if choose == 1:
        print("Выберите действие:\n1. Добавить строку\n2. Удалить строку")
        studentChoose = int(input("Выбор: "))
        if studentChoose == 1:
            try:
                with connect(
                        host="localhost",
                        user="root",
                        password="",
                        database="db_students"
                ) as connection2:
                    firstname = input("Имя: ")
                    lastname = input("\nФамилия: ")
                    age = input("\nВозраст: ")
                    group_id = input("\nНомер группы: ")
                    insert_student_query = """INSERT INTO students (firstname, lastname, age, group_id) VALUES (%s,
                    %s,%s,%s) """
                    record = [(firstname, lastname, age, group_id)]
                    with connection2.cursor() as cursor2:
                        cursor2.executemany(insert_student_query,
                                            record)
                        connection2.commit()
                        select_students_query = "SELECT * FROM students"
                        with connection2.cursor() as cursor2:
                            cursor2.execute(select_students_query)
                            result = cursor2.fetchall()
                            for row in result:
                                print(row)
            except Error as e:
                print(e)
        elif studentChoose == 2:
            try:
                with connect(
                        host="localhost",
                        user="root",
                        password="",
                        database="db_students"
                ) as connection3:
                    deleteRow = int(input("Какую строку удалить: "))
                    delete_student_query = "DELETE FROM students WHERE student_id = %s"
                    foreignkey_checks_query = "SET FOREIGN_KEY_CHECKS=0"
                    record = [(deleteRow,)]
                    with connection3.cursor() as cursor3:
                        cursor3.execute(foreignkey_checks_query)
                        cursor3.commit()
                        cursor3.executemany(delete_student_query, record)
                        connection3.commit()
                        select_students_query = "SELECT * FROM students"
                        with connection3.cursor() as cursor3:
                            cursor3.execute(select_students_query)
                            result = cursor3.fetchall()
                            for row in result:
                                print(row)
            except Error as er:
                print(er)
    elif choose == 2:
        print("Выберите действие:\n1. Добавить строку\n2. Удалить строку")
        groupChoose = int(input("Выбор: "))
        if groupChoose == 1:
            try:
                with connect(
                        host="localhost",
                        user="root",
                        password="",
                        database="db_students"
                ) as connection4:
                    group_name = input("Имя группы: ")
                    insert_group_query = """INSERT INTO gruppa (group_name) VALUES (%s) """
                    record2 = [(group_name,)]
                    with connection4.cursor() as cursor4:
                        cursor4.executemany(insert_group_query,
                                            record2)
                        connection4.commit()
                        select_gruppa_query = "SELECT * FROM gruppa"
                        with connection4.cursor() as cursor4:
                            cursor4.execute(select_gruppa_query)
                            result = cursor4.fetchall()
                            for row in result:
                                print(row)
            except Error as e:
                print(e)
        elif groupChoose == 2:
            try:
                with connect(
                        host="localhost",
                        user="root",
                        password="",
                        database="db_students"
                ) as connection5:
                    deleteRow = int(input("Какую строку удалить: "))
                    delete_group_query = "DELETE FROM gruppa WHERE group_id = %s"
                    record = [(deleteRow,)]
                    foreignkey_checks_query = "SET FOREIGN_KEY_CHECKS=0"
                    with connection5.cursor() as cursor5:
                        cursor5.execute(foreignkey_checks_query)
                        connection5.commit()
                        cursor5.executemany(delete_group_query, record)
                        connection5.commit()
                        select_group_query = "SELECT * FROM gruppa"
                        with connection5.cursor() as cursor5:
                            cursor5.execute(select_group_query)
                            result = cursor5.fetchall()
                            for row in result:
                                print(row)
            except Error as er:
                print(er)
    elif choose == 3:
        print("Выберите действие:\n1. Добавить строку\n2. Удалить строку")
        subjectChoose = int(input("Выбор: "))
        if subjectChoose == 1:
            try:
                with connect(
                        host="localhost",
                        user="root",
                        password="",
                        database="db_students"
                ) as connection6:
                    subject_name = input("Название предмета: ")
                    insert_subject_query = """INSERT INTO subjects (subject_name) VALUES (%s) """
                    record = [(subject_name,)]
                    with connection6.cursor() as cursor6:
                        cursor6.executemany(insert_subject_query,
                                            record)
                        connection6.commit()
                        select_subject_query = "SELECT * FROM subjects"
                        with connection6.cursor() as cursor6:
                            cursor6.execute(select_subject_query)
                            result = cursor6.fetchall()
                            for row in result:
                                print(row)
            except Error as e:
                print(e)
        elif subjectChoose == 2:
            try:
                with connect(
                        host="localhost",
                        user="root",
                        password="",
                        database="db_students"
                ) as connection7:
                    deleteRow = int(input("Какую строку удалить: "))
                    delete_subject_query = "DELETE FROM subjects WHERE subject_id = %s"
                    record = [(deleteRow,)]
                    foreignkey_checks_query = "SET FOREIGN_KEY_CHECKS=0"
                    with connection7.cursor() as cursor7:
                        cursor7.execute(foreignkey_checks_query)
                        connection7.commit()
                        cursor7.executemany(delete_subject_query, record)
                        connection7.commit()
                        select_subject_query = "SELECT * FROM subjects"
                        with connection7.cursor() as cursor7:
                            cursor7.execute(select_subject_query)
                            result = cursor7.fetchall()
                            for row in result:
                                print(row)
            except Error as er:
                print(er)
    elif choose == 4:
        print("Выберите действие:\n1. Добавить строку\n2. Удалить строку")
        markChoose = int(input("Выбор: "))
        if markChoose == 1:
            try:
                with connect(
                        host="localhost",
                        user="root",
                        password="",
                        database="db_students"
                ) as connection8:
                    student_id = input("Номер студента: ")
                    subject_id = input("\nНомер предмета: ")
                    mark = input("\nОценка: ")
                    insert_mark_query = """INSERT INTO marks (student_id, subject_id, mark) VALUES (%s, %s, %s) """
                    record = [(student_id, subject_id, mark)]
                    with connection8.cursor() as cursor8:
                        cursor8.executemany(insert_mark_query,
                                            record)
                        connection8.commit()
                        select_mark_query = "SELECT * FROM marks"
                        with connection8.cursor() as cursor8:
                            cursor8.execute(select_mark_query)
                            result = cursor8.fetchall()
                            for row in result:
                                print(row)
            except Error as e:
                print(e)
        elif markChoose == 2:
            try:
                with connect(
                        host="localhost",
                        user="root",
                        password="",
                        database="db_students"
                ) as connection9:
                    deleteRow = int(input("Какую строку удалить: "))
                    delete_mark_query = "DELETE FROM marks WHERE mark_id = %s"
                    record = [(deleteRow,)]
                    foreignkey_checks_query = "SET FOREIGN_KEY_CHECKS=0"
                    with connection9.cursor() as cursor9:
                        cursor9.execute(foreignkey_checks_query)
                        connection9.commit()
                        cursor9.executemany(delete_mark_query, record)
                        connection9.commit()
                        select_mark_query = "SELECT * FROM marks"
                        with connection9.cursor() as cursor9:
                            cursor9.execute(select_mark_query)
                            result = cursor9.fetchall()
                            for row in result:
                                print(row)
            except Error as er:
                print(er)
    return 0


main()
