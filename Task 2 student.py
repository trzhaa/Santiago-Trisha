class Student:
        def __init__(self, name, age, course):
         self.name = name
         self.age = age
         self.course = course
    
        def introduce(self):
           print(f"Hello, my name is {self.name}. I am {self.age} years old, and I am studying {self.course}.")

student1 = Student("Trisha Santiago", 20, "Diploma Information Technology")

student1.introduce()