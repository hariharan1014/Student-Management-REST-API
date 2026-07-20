from student.student import Student
from utils.validation import check_int,check_str,check_phone
class Management:
    def __init__(self,file='data/student_list.txt'):
        self.students=[]
        self.rules = {
            "roll_num": check_int,
            "first_name": check_str,
            "last_name": check_str,
            "department": check_str,
            "age": check_int,
            "city": check_str,
            "phone_num": check_phone
        }
        self.filename = file
        self.load_file()
    def load_file(self):
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    if line.strip():
                        data=line.strip().split(',')
                        student=Student(data[0],data[1],data[2],data[3],data[4],data[5],data[6])
                        self.students.append(student)
        except FileNotFoundError:
            self.students=[]
    def save_file(self):
        with open(self.filename, 'w') as file:
            for s in self.students:
                file.write(f"{s.roll_num},{s.first_name},{s.last_name},{s.department},{s.age},{s.city},"
                           f"{s.phone_num}\n")
    def add_student(self,data):
            valid,message= self.validate_data(data)
            if not valid:
                return {
                    "success" :False ,
                    "status" : 400,
                    "message" : message
                }
            valid,duplicate_check_msg= self.is_duplicate_roll_num(int(data["roll_num"]))
            if not valid:
                return {
                    "success" :False,
                    "status" : 409,
                    "message" : duplicate_check_msg
                }
            self.students.append(Student(data['roll_num'],data['first_name'],data['last_name'],data['department'],
                                         data['age'],data['city'],data['phone_num']))
            self.save_file()
            return { "success" : True,
                        "message" : f"Student added successfully",
                        "status" : 201,
                        "student":{
                        "department" : data['department'].strip(),
                        "last_name": data['last_name'].strip(),
                        "first_name": data['first_name'].strip(),
                        "roll_num": data['roll_num'].strip(),
                                }
                    }
    def validate_data(self,data):
        for key in self.rules:
            if key not in data:
                return  False, f"{key} is missing"
            checker=self.rules[key]
            valid,message=checker(data[key])
            if not valid:
                return  False, message
        return True,None
    def is_duplicate_roll_num(self,roll_num):
        for student in self.students:
            if roll_num == student.roll_num:
                return  False, f"Student with roll number {student.roll_num} already exists"
        return True,None