#This program creates students and a course and adds students to the course 


class Student:
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade #1 - 100

    def get_name(self):
        return self.name
    
    def get_grade(self):
        return self.grade  
    

class Course:
    def __init__(self,name,max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self,student):
        
        if len(self.students) < self.max_students:
            self.students.append(student)
            
            return True
        return False
        
    
    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()

        return value/len(self.students)

s1 = Student("Asad",22,95)    
s2 = Student("Milku",5,50)    
s3 = Student("Meme",20,45)    


stud1 = Student("Chomp",45,40)
stud2 = Student("Shompie",5,69)

#
course = Course("CompSci", 2)

course.add_student(s1)
course.add_student(s2)

print(course.get_average_grade())
