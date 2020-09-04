import mysql.connector


class MyDb:
    def __init__(self):
        self.my_connection = mysql.connector.connect(user="root", password="password1234", host='127.0.0.1',
                                                     database="student_sys", auth_plugin='mysql_native_password')
        self.my_cursor = self.my_connection.cursor()

    def aur(self, qry, values):
        self.my_cursor.execute(qry, values)
        self.my_connection.commit()

    def show_data(self, qry):
        self.my_cursor.execute(qry)
        data = self.my_cursor.fetchall()
        return data

    def show_data_from_p(self, qry, value):
        self.my_cursor.execute(qry, value)
        data = self.my_cursor.fetchall()
        return data

    def truncate_students(self):
        qry = "TRUNCATE TABLE students_info"
        self.my_cursor.execute(qry)
        self.my_connection.commit()

