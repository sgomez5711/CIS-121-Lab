# Question 1
class Student:
    def __intit__(self, name, major):
        self.name = name
        self.major = major

    def get_major(self):
        return self.major
    
    def set_major(self, new_major):
        self.major = new_major

    def __str__(self):
        return (f"{self.name}: Major: {self.major}")
    

class Course:
    def __init__(self, course_name, course_number):
            self.course_name = course_name
            self.course_number = course_number
            self.students = []

    def get_number(self):
            return self.course_number
        
    def set_number(self, new_number):
            self.course_number = new_number

    def add_student(self, student):
            self.students.append(student)

    def show_student_enrollment(self):
            for s in self.students:
                print(s)

    def __str__(self):
            return (f" {self.course_name} ({self.course_number})")
    
    
course1= Course("Intro to Python", "CIS 121")

student1= Student("Steve", "IT")
student2 = Student("Bob", "Computer Science")

course1.add_student(student1)
course1.add_student(student2)
        

#Question 2

class Duck:
    def __init__(self, name, color):
            self.name = name
            self.color = color
        
    def get_color(self):
            return self.color

    def set_color(self, new_color):
          self.color = new_color

    def speak(self):
          print("Quck!")

    def __str__(self):
          return (f"{self.name}, Color: {self.color}")  
    
class Pond:
    def __init__(self, name):
            self.name = name
            self.ducks = []

    def add_ducks(self, duck):
          self.ducks.append(duck)

    def ducks_quack(self):
          for d in self.ducks:
                d.speak()
    
    def __str__(self):
          return (f"Pond: {self.name} with {self.ducks} ducks")
    
    
pond1 = Pond("Great Pond")

duck1 = Duck("Chicken", "white")
duck2 = Duck("Crow", "Black")

pond1.add_duck(duck1)
pond2.add_duck(duck2)

pond1.ducks_quack()

#Question 3

class Lion:
    def __init__(self, name, gender)
            self.name = name
            self.gender = gender
        
    def get_name(self):
          return self.name
    
    def set_name(self, new_name):
          self.name = new_name

    def roar(self):
          print("Roar!")

    def __str__(self):
          return (f"{self.name} {self.gender}")
    

class Zoo:
    def __init__(self, location):
            self.location = location
            self.lions = []
    
    def add_lion(self, lion):
          self.lions.append(lion)

    def lions_roar(self):
          for 1 in self.lions:
                1.roar()

    def count_lions(self):
        males = 0
        females = 0
        for 1 in self.lions:
            if 1.gender.lower() == "male":
                males += 1
            elif 1.gender.lower() == "femmales":
                females += 1
        print(f"{males} male, {females} female")

    def __str__(self):
          return (f"Zoo at {self.location}")
    
    
z = Zoo("Mankato Zoo")
L1 = Lion("Simba", "Male")
L2 = Lion("Nala", "Female")

z.add_lion(L1)
z.add_lion(L2)

z.lions_roar()
z.count_lions()

# Question 4

class Employee:
    def __init__(self, name, position):
            self.name = name
            self.position = position

    def get_position(self):
          return self.position
    
    def set_position(self, new_position):
          self.position = new_position

    def __str__(self):
          return (f"{self.name}" - {self.position})
    
    