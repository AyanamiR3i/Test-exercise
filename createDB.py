from flask_mysqldb import MySQL
from mysql.connector import connect, Error
from flask import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)

try:
    with connect(
            host="localhost",
            user=input("Введите имя пользователя: "),
            password="",
    ) as connection:
        createdb_query = "CREATE DATABASE db_students;"
        with connection.cursor() as cursor:
            cursor.execute(createdb_query)
            #cursor.commit()
            create_tables_query = "USE db_students;" \
                                  "CREATE TABLE gruppa(" \
                                  "group_id INT PRIMARY KEY AUTO_INCREMENT," \
                                  "group_name NVARCHAR(30)" \
                                  ");" \
                                  "CREATE TABLE subjects(" \
                                  "subject_id INT PRIMARY KEY AUTO_INCREMENT," \
                                  "subject_name NVARCHAR(30)" \
                                  ");" \
                                  "CREATE TABLE students(" \
                                  "student_id INT PRIMARY KEY AUTO_INCREMENT," \
                                  "firstname NVARCHAR(30)," \
                                  "lastname NVARCHAR(30)," \
                                  "age INT," \
                                  "group_id INT," \
                                  "FOREIGN KEY(group_id) REFERENCES gruppa(group_id)" \
                                  ");" \
                                  "CREATE TABLE marks(" \
                                  "mark_id INT PRIMARY KEY AUTO_INCREMENT," \
                                  "student_id INT," \
                                  "subject_id INT," \
                                  "mark INT" \
                                  "FOREIGN KEY (student_id) REFERENCES students(student_id)," \
                                  "FOREIGN KEY (subject_id) REFERENCES subjects(subject_id)" \
                                  ");"
            cursor.execute(create_tables_query)
            #cursor.commit()
            insert_gruppa_query = "use db_students;" \
                                  "INSERT INTO gruppa (group_name) VALUES " \
                                  "('907ca')," \
                                  "('907cb')," \
                                  "('901a')," \
                                  "('901b')," \
                                  "('901c')," \
                                  "('801a')," \
                                  "('801b')," \
                                  "('801c')," \
                                  "('703a')," \
                                  "('703ca');"
            cursor.execute(insert_gruppa_query)
            cursor.commit()
            insert_subject_query = "use db_students;" \
                                   "INSERT INTO subjects (subject_name) VALUES " \
                                   "('Математика')," \
                                   "('Русский язык')," \
                                   "('Программирование')," \
                                   "('Нейронные сети')," \
                                   "('Алгоритмы')," \
                                   "('Тестирование ПО')," \
                                   "('Физическая культура')," \
                                   "('Экономика')," \
                                   "('Философия')," \
                                   "('Менеджмент');"
            cursor.execute(insert_subject_query)
            cursor.commit()
            insert_students_query = "use db_students;" \
                                    "INSERT INTO students (firstname, lastname, age, group_id) VALUES " \
                                    "('Анатолий', 'Степанов', 19, 4)," \
                                    "('Евгений', 'Смирнов', 18, 8)," \
                                    "('Екатерина', 'Борисова', 18, 6)," \
                                    "('Александра', 'Петровская', 18, 1)," \
                                    "('Никита', 'Попов', 20, 4)," \
                                    "('Михаил', 'Алексеев', 21, 6)," \
                                    "('Евгения', 'Данилова', 19, 9)," \
                                    "('Максим', 'Кузнецов', 18, 3)," \
                                    "('Светлана', 'Прокофьева', 19, 7)," \
                                    "('Владимир', 'Волков', 21, 2);"
            cursor.execute(insert_students_query)
            cursor.commit()
            insert_marks_query = "use db_students;" \
                                 "INSERT INTO marks (student_id, subject_id, mark) VALUES " \
                                 "(3, 1, 5)," \
                                 "(2, 9, 5)," \
                                 "(8, 1, 4)," \
                                 "(1, 6, 3)," \
                                 "(5, 4, 4)," \
                                 "(7, 4, 2)," \
                                 "(9, 3, 2)," \
                                 "(4, 7, 5)," \
                                 "(1, 9, 3)," \
                                 "(5, 3, 3);"
            cursor.execute(insert_marks_query)
            cursor.commit()
            for db in cursor:
                print(db)

except Error as e:
    print(e)
