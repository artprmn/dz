import sqlite3

# Подключение к базе данных
conn = sqlite3.connect('university.db')

# Создание курсора для выполнения SQL-запросов
cursor = conn.cursor()

# Добавление данных в таблицу Courses
cursor.execute("INSERT INTO Courses VALUES (1, 'python', '2021-07-21', '2021-08-21')")
cursor.execute("INSERT INTO Courses VALUES (2, 'java', '2021-07-13', '2021-08-16')")

# Добавление данных в таблицу Students
cursor.execute("INSERT INTO Students VALUES (1, 'Max', 'Brooks', 24, 'Spb')")
cursor.execute("INSERT INTO Students VALUES (2, 'John', 'Stones', 15, 'Spb')")
cursor.execute("INSERT INTO Students VALUES (3, 'Andy', 'Wings', 45, 'Manchester')")
cursor.execute("INSERT INTO Students VALUES (4, 'Kate', 'Brooks', 34, 'Spb')")

# Добавление данных в таблицу Student_courses
cursor.execute("INSERT INTO Student_courses VALUES (1, 1)")
cursor.execute("INSERT INTO Student_courses VALUES (2, 1)")
cursor.execute("INSERT INTO Student_courses VALUES (3, 1)")
cursor.execute("INSERT INTO Student_courses VALUES (4, 2)")

# Сохранение изменений
conn.commit()

# Закрытие соединения с базой данных
conn.close()
