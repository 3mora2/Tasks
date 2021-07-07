import mysql.connector
from time import sleep
import os
import re

class Main_DB:
    def __init__(self, user_id):
        self.user_id = user_id
        self.database = mysql.connector.connect(host="localhost", user="root", passwd="", database="certificates")

    def check_school(self, name):
        cursor = self.database.cursor()
        sql = f"SELECT * FROM schools WHERE name='{name}' AND user_id='{self.user_id}' LIMIT 1"
        cursor.execute(sql)
        return cursor.fetchall()

    def add_school(self, name, stage):
        result = self.check_school(name)
        if result:
            print('- Found School ')
            return result[0][0]
        else:
            cursor = self.database.cursor()
            sql = f"INSERT INTO schools (name, stage,user_id) VALUES ('{name}', {stage}, '{self.user_id}')"
            # val = (name, stage, self.user_id)
            cursor.execute(sql)  # , val)
            school_id = cursor.lastrowid
            self.database.commit()
            return school_id

    def check_class(self, class_id, num, school):
        cursor = self.database.cursor()
        sql = f"SELECT * FROM classes WHERE class_id ='{class_id}' AND num='{str(num)}' AND school_id='{str(school)}' LIMIT 1"
        cursor.execute(sql)
        return cursor.fetchall()

    def add_class(self, class_id, class_name, section_name, num, school):
        result = self.check_class(class_id=class_id, num=num, school=school)
        if result:
            print('- Found Class ')
            return False
        else:
            cursor = self.database.cursor()
            sql = "INSERT INTO classes (name, section_name, class_id, num, school_id) VALUES (%s, %s, %s, %s, %s)"
            val = (class_name, section_name, class_id, num, school)
            cursor.execute(sql, val)
            self.database.commit()
            print("- one class inserted")

    def select_class_info(self, class_id, num, school_id):
        cursor = self.database.cursor()
        sql = f"SELECT * FROM classes WHERE class_id='{str(class_id)}' AND school_id='{str(school_id)}' AND num='{str(num)}' LIMIT 1"
        cursor.execute(sql)
        result = cursor.fetchall()
        if result:
            return result[0]

    def student_exist(self, std_id, school_id):
        cursor = self.database.cursor()
        sql = f"SELECT * FROM students WHERE student_id ='{std_id}' AND school_id='{str(school_id)}' LIMIT 1"
        cursor.execute(sql)
        result = cursor.fetchall()
        if result:
            return True
        else:
            return False

    def add_student(self, std_id, std_name, phone, class_id, class_num, school_id, high=False):
        cursor = self.database.cursor()
        sql = f"SELECT * FROM students WHERE student_id ='{std_id}' AND school_id='{str(school_id)}' LIMIT 1"
        cursor.execute(sql)
        result = cursor.fetchall()
        if result:
            print("- Found")
            return False
        else:
            if high:
                sql = f"INSERT INTO students (student_id, name, phone, class_num, school_id) " \
                      f"VALUES ('{std_id}', '{std_name}', '{phone}', '{class_num}', '{school_id}')"
            else:
                sql = f"INSERT INTO students (student_id, name, phone, class_id, class_num, certificate, school_id) " \
                  f"VALUES ('{std_id}', '{std_name}', '{phone}', '{class_id}', '{class_num}', '{str(std_id) + '.pdf'}','{school_id}')"
            cursor.execute(sql)
            self.database.commit()
            print("- One Student Inserted....")

    def update_student(self, name, school_id, std_id):
        cursor = self.database.cursor()
        # sql = f"SELECT student_id FROM students WHERE name ='{name}' AND school_id='{str(school_id)}' LIMIT 1"
        # cursor.execute(sql)
        # # print(name, school_id)
        # try:
        #     std_id = cursor.fetchone()[0]
        # except Exception as e:
        #     print(e)
        #     return False
        # print(std_id)
        # Filter Name
        pdf = ''.join(re.findall(r'\w+', std_id)) + ".pdf"
        # sql = f'''
        #         UPDATE `students` SET `certificate`= CONCAT((
        #         SELECT `student_id` FROM `students` WHERE name='{name}' AND school_id='{school_id}'),'.pdf');'''
        sql = f'UPDATE students SET certificate= "{pdf}" WHERE student_id = "{std_id}"'
        cursor.execute(sql)
        self.database.commit()
        print("- One Student Update....")
        return pdf

    def download_wait(self, directory, timeout, number_file=None):
        seconds = 0
        dl_wait = True
        while dl_wait and seconds < timeout:
            sleep(1)
            dl_wait = False
            files = os.listdir(directory)
            if number_file and len(files) == number_file:
                dl_wait = True
                print('- Yet')
                continue
            sleep(6)
            seconds += 6
            for file_name in files:
                if file_name.endswith('.crdownload'):
                    dl_wait = True
                    print('- Yet : .crdownload')

            seconds += 1
        return seconds

    def download_wait_2(self, directory, filenames):
        while True:
            files = os.listdir(directory)
            new_l = set(files)-set(filenames)
            if len(new_l) != 0:
                if list(new_l)[0].endswith('.crdownload'):
                    sleep(6)
                    print('- Yet : .crdownload')
                else:
                    break
            else:
                print('- Yet')
                sleep(4)


