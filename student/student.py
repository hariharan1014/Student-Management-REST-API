class Student:
    def __init__(self, roll_num,first_name,last_name,department,age,city,phone_num):
        self.roll_num = int(str(roll_num).strip())
        self.first_name = first_name.upper().strip()
        self.last_name = last_name.upper().strip()
        self.department = department.upper().strip()
        self.age = int(str(age).strip())
        self.city = city.upper().strip()
        self.phone_num = int(str(phone_num).strip())