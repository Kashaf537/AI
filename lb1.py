class Person:
    def __init__(self,name,age,program):
        self.name=name
        self.age=age
        self.program=program
    
    def display(self):
        print("Name is "+self.name+"," +"Age is: "+" "+str(self.age)+" , "+"program is "+self.program)

p1=Person("Sara",20,"AI")
p1.display()


#ii)

def student_data(student_id, student_name,student_class):
    print("Student ID: ",student_id)
    if student_name:
        print("Student name: ",student_name)
    elif  student_class:
        print("Student Class:", student_class)

student_data(101,"","")
student_data(102,"Ali","")
student_data(103,"Sara","FA24-BAI-031")


#iii)
class Student:
    pass

print("Type: ",type(Student))
print("Dict keys: ",Student.__dict__.keys())
print("Module:",Student.__module__)


#iv)
class Student:
    pass
class Marks:
    pass
s=Student()
m=Marks()

print(isinstance(s,Student))
print(isinstance(m,Marks))
print(isinstance(m,Student))
print(issubclass(Student,object))
print(issubclass(Marks,object))


#v)
class Student:
    def __init__(self, name, marks):
        self.student_name = name
        self.marks = marks

s = Student("Ali", 90)
print("Original:", s.student_name, s.marks)

s.student_name = "Sara"
s.marks = 95
print("Modified:", s.student_name, s.marks)


#vi)
class Student:
    def __init__(self,sid,name):
        self.student_id=sid
        self.student_name=name

s=Student(108,"Ali")

s.student_class="AI(A)"

print("Attributes after adding the class: ",s.__dict__)

del s.student_name
print("Attributes after removing name:",s.__dict__)


#vii)
class Student:
    def __init__(self,sid,name):
        self.student_id=sid
        self.student_name=name
        self.student_class="AI"

    def display(self):
        print("Name: "+" "+self.student_name+" "+"StudentID"+" "+str(self.student_id)+" "+"class"+" "+self.student_class)

s1=Student(101,"Sara")
s1.display()

#viii)
class Student:
    def __init__(self,sid,name,marks):
        self.student_id=sid
        self.student_name=name
        self.marks=marks

    def display(self):
        print("Student1\n")
        for attr,val in self.__dict__.items():
            print(attr,":",val)
    def display2(self):

        print("Student2\n")
        for at,value in self.__dict__.items():
            print(at,":",value)
        

student1=Student(101,"Ali",90)
student2=Student(102,"Sara",95)

student1.display()
student2.display2()

#9)
import sys

class Student:
    def __init__(self, sid, name):
        self.student_id = sid
        self.student_name = name

s = Student(101, "Ali")
print("Memory size of object:", sys.getsizeof(s))
print("Memory size of dict:", sys.getsizeof(s.__dict__))

#10)
class Student:
    __slots__ = ['student_id', 'student_name']  
    def __init__(self, sid, name):
        self.student_id = sid
        self.student_name = name

s = Student(101, "Ali")

import sys
print("Memory size with slots:", sys.getsizeof(s))
