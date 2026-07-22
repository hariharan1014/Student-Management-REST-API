from student.student import Student,format_int,format_str
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
            found= self.find_student_by_roll_num(int(data["roll_num"]))
            if found:
                return {
                    "success" :False,
                    "status" : 409,
                    "message" :f"Student with roll number {data['roll_num']} already exists"
                }
            std=Student(data['roll_num'],data['first_name'],data['last_name'],data['department'],
                                         data['age'],data['city'],data['phone_num'])
            self.students.append(std)
            self.save_file()
            dictionary=std.to_dict()
            return { "success" : True,
                        "message" : f"Student added successfully",
                        "status" : 201,
                        "student": dictionary
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
    def find_student_by_roll_num(self,roll_num):
        for student in self.students:
            if roll_num == student.roll_num:
                return  student
        return None
    def get_students(self):
        return { "success" : True,
                "status" : 200,
                "students" : [student.to_dict() for student in self.students]
        }
    def get_student_by_roll_num(self,roll_num):
        student=self.find_student_by_roll_num(roll_num)
        if student is not None:
                return {"success": True,
                        "status": 200,
                        "student": student.to_dict()
                        }
        return {"success": False,
                "status" : 404,
                "message" : f"Student with roll number {roll_num} does not exist"
                }
    def update_student(self,data,roll_num):
        student=self.find_student_by_roll_num(roll_num)
        if student is not None:
            for key in data:
                if key not in self.rules:
                    return {
                        "success" : False,
                        "status" : 400,
                        "Unknown field" : f"Unknown field: {key}"
                    }
            for key in data:
                if key == "roll_num":
                    return {
                            "success": False,
                            "status": 400,
                            "message": "Roll number cannot be modified."
                            }
                if key in self.rules:
                    checker=self.rules[key]
                    result,message=checker(data[key])
                    if  not result:
                        return {"success" : False,
                                "status" : 400,
                                "message" : message
                           }
            student.update(data)
            self.save_file()
            return { "success" : True,
                     "status" : 200,
                     "message" : "Student updated successfully",
                     "student": student.to_dict()
                     }
        else:
            return {
                "success" : False,
                "status" : 404,
                "message" : f"Student with roll number {roll_num} does not exist for update."
            }
    def delete_student(self,roll_num):
        student=self.find_student_by_roll_num(roll_num)
        if student is not None:
            self.students.remove(student)
            self.save_file()
            return { "success" : True,
                     "status" : 200,
                     "message" : "Student deleted successfully"
                     }
        else:
            return {
                "success" : False,
                "status" : 404,
                "message" : f"Student with roll number {roll_num} does not exist for delete."
            }
    def search_students(self,field,value):
        result=[]
        for student in self.students:
            student_value = getattr(student, field)
            if student_value == value:
                result.append(student.to_dict())
        if not result:
            return {
                "success" : False,
                "status" : 404,
                "message": f"No students found for {field} '{value}'."
            }
        return { "success" : True,
                 "status" : 200,
            "students" : result
                 }
    def sort_students(self,field):
        if  field not in self.rules:
            return {
                "success" : False,
                "status" : 400,
                "message" : f"Unknown field: {field}"
            }
        elif field == "phone_num":
            return {
                "success" : False,
                "status" : 400,
                "message" : "access restricted to phone number."
            }

        sorted_object=sorted(
            self.students,
            key=lambda student: getattr(student, field)
        )
        result = [student.to_dict() for student in sorted_object]
        return { "success" : True,
                 "status" : 200,
                 "students" : result
                 }
    def filter_students(self,filters):
        for field in filters:
            if field not in self.rules:
                return {
                    "success" : False,
                    "status" : 400,
                    "message" : f"Unknown field: {field}"
                }
        result=[]
        for student in self.students:
            match=True
            for field,value in filters.items():
                if field == "roll_num" or field == "age":
                    formatted_value=format_int(value)
                else:
                    formatted_value=format_str(value)
                if getattr(student,field) != formatted_value :
                    match=False
                    break
            if match:
                result.append(student.to_dict())
        if not result:
            return {
                "success": False,
                "status": 404,
                "students": []
            }
        return { "success" : True,
                 "status" : 200,
                 "students" : result
            }

