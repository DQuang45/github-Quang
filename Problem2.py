class Student:
    def __init__(self, name, major, ID):
        self.name = name
        self.major = major
        self.ID = ID

class StudentPartTime(Student):
    StudentPT = 0  
    def __init__(self, name, major, ID, maxhours, minhours):
        super().__init__(name, major, ID)
        StudentPartTime.StudentPT += 1  
        self.maxhours = maxhours
        self.minhours = minhours
    def count():
        return StudentPartTime.StudentPT    
     
class StudentFullTime(Student):
    def __init__(self, name, major, ID,project):
        super().__init__(name, major, ID)
        self.project = project
         
hocvien1 = StudentPartTime("Nguyen Van A", "IT", "IT001" , 20, 10)
hocvien2 = StudentPartTime("Nguyen Van B", "IT", "IT002" , 20, 10)
hocvien3 = StudentPartTime("Nguyen Van C", "IT", "IT003" , 20, 10)


print(hocvien1.name, hocvien1.major, hocvien1.ID, hocvien1.maxhours, hocvien1.minhours)
print(hocvien2.name, hocvien2.major, hocvien2.ID, hocvien2.maxhours, hocvien2.minhours)
print(hocvien3.name, hocvien3.major, hocvien3.ID, hocvien3.maxhours, hocvien3.minhours)
print("So hoc vien part-time la: ", StudentPartTime.count())
