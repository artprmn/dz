import sqlite3


class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create_tables(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Students
                              (id INTEGER PRIMARY KEY,
                               name TEXT,
                               surname TEXT,
                               age INTEGER,
                               city TEXT)''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Courses
                              (id INTEGER PRIMARY KEY,
                               name TEXT,
                               time_start TEXT,
                               time_end TEXT)''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Student_courses
                              (student_id INTEGER,
                               course_id INTEGER,
                               FOREIGN KEY (student_id) REFERENCES Students(id),
                               FOREIGN KEY (course_id) REFERENCES Courses(id),
                               PRIMARY KEY (student_id, course_id))''')

    def insert_student(self, name, surname, age, city):
        self.cursor.execute("INSERT INTO Students (name, surname, age, city) VALUES (?, ?, ?, ?)",
                            (name, surname, age, city))
        self.conn.commit()

    def insert_course(self, name, time_start, time_end):
        self.cursor.execute("INSERT INTO Courses (name, time_start, time_end) VALUES (?, ?, ?)",
                            (name, time_start, time_end))
        self.conn.commit()

    def enroll_student_in_course(self, student_id, course_id):
        self.cursor.execute("INSERT INTO Student_courses (student_id, course_id) VALUES (?, ?)",
                            (student_id, course_id))
        self.conn.commit()

    def get_students_over_30(self):
        self.cursor.execute("SELECT * FROM Students WHERE age > 30")
        return self.cursor.fetchall()

    def get_students_on_python_course(self):
        self.cursor.execute('''SELECT Students.* FROM Students
                               JOIN Student_courses ON Students.id = Student_courses.student_id
                               JOIN Courses ON Student_courses.course_id = Courses.id
                               WHERE Courses.name = 'python' ''')
        return self.cursor.fetchall()

    def get_students_on_python_course_in_spb(self):
        self.cursor.execute('''SELECT Students.* FROM Students
                               JOIN Student_courses ON Students.id = Student_courses.student_id
                               JOIN Courses ON Student_courses.course_id = Courses.id
                               WHERE Courses.name = 'python' AND Students.city = 'Spb' ''')
        return self.cursor.fetchall()

    def close_connection(self):
        self.conn.close()
