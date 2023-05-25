import sqlite3

# Подключение к базе данных
conn = sqlite3.connect('university.db')

# Создание курсора для выполнения SQL-запросов
cursor = conn.cursor()

# Создание таблицы Students
cursor.execute('''CREATE TABLE Students
                  (id INTEGER PRIMARY KEY,
                   name TEXT,
                   surname TEXT,
                   age INTEGER,
                   city TEXT)''')

# Создание таблицы Courses
cursor.execute('''CREATE TABLE Courses
                  (id INTEGER PRIMARY KEY,
                   name TEXT,
                   time_start TEXT,
                   time_end TEXT)''')

# Создание таблицы Student_courses
cursor.execute('''CREATE TABLE Student_courses
                  (student_id INTEGER,
                   course_id INTEGER,
                   FOREIGN KEY (student_id) REFERENCES Students(id),
                   FOREIGN KEY (course_id) REFERENCES Courses(id),
                   PRIMARY KEY (student_id, course_id))''')

# Закрытие соединения с базой данных
conn.close()
