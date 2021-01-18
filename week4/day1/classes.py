class Student:
    student_id = 0

    def __init__(self,name,last_name,group):
        self.name = name
        self.last_name = last_name
        self.group = group
        Student.student_id +=1

student1 = Student('akylbek','melisov','python')
print(student1.student_id,student1.name)
student2 = Student('jarkynai','satarova','python')
print(student2.student_id,student2.name)
student3 = Student('aigerim','kashkarbekova','python')
print(student3.student_id,student3.name)
student4 = Student('nurjanat','abaeva','python')
print(student4.student_id,student4.name)
student5 = Student('baiel','nurmatbek uulu','python')
print(student5.student_id,student5.name)