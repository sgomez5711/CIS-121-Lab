#Lecture 11/6/2025 Practiced Quiz Questions

class Song:
    def __init__(self, title, artist, duration_seconds):
        self.title = title
        self.artist = artist
        self.duration_seconds = duration_seconds

    def get_title(self):
        return self.title
    
    def get_artist(self):
        return self.artist
    
    def get_duration_seconds(self):
        return self.duration_seconds
    
    def set_title(self, value):
        self.title = value

    def set_artist(self, value):
        self.artist = value

    def set_duration_seconds(self, value):
        if value > 0:
            self.duration_seconds = value

    def __str__(self):
        return (f" The title is {self.title} by {self.artist} and lasts for {self.duration_seconds} seconds.")
    
song1 = Song("See You Again", "Charlie Puth", 240)

print(song1)






class Employee:
    def __init(self, name, title, salary):
        self.name = name
        self.title = title
        self.salary = salary

    def get_name(self):
        return self.name
    def get_title(self):
        return self.title
    def get_salary(self):    
        return self.salary 
    
    def set_name(self, value):
        self.name = value
    def set_title(self, value):
        self.title = value
    def set_salary(self, value):
        if value > 0:
            self.salary = value

    def greeting(self):
    return (f" Hello. My name is {self.name}. I'm the {self.title}")

    def request_raise(self):
        new_amount = self.salary * 1.06
        return (f"I'm currently making ${self.salary}. I'd like new salary of ${new_amount} ")
    
 employee1 = Employee("John", "Manager", 70000)

print(employee1.greeting())
print(empoyee1.request_raise())







class Student:
    def __init__(self, name, major, GPA):
        self.name = name
        self.major = major
        self.GPA = GPA

    def get_name(self):
        return self.name
    def get_major(self):
        return self.major
    def get_GPA(self):
        return self.GPA
    
    def set_name(self, value):
        self.name = value

    def set_major(self, value):
        self.major = value

    def set_GPA(self, value):
        if 0 <= self.GPA <= 4.0:
            self.GPA = value

    def introduce(self):
        return (f" Hi, I'm {self.name}. I'm studying {self.major}.")
    
    def study_for_exam(self):
        new_GPA = self.GPA + 0.2
        return (f" I'm hitting the books! My GPA increased from {self.GPA} to {new_GPA}. ")
    
student1 = Student("James", "Computer Science", 3.5)

print(student1.introduce())
print(student1.study_for_exam())

class Book:
    def __init__(self, title, author, page_count):
        self.name = name
        self.title = title
        self.page_count = page_count

    def get_name(self):
        return self.name
    def get_author(self):
        return self.author
    def get_page_count(self):
        return self.page_count
    
    def set_name(self, value):
        self.name = value

    def set_author(self, value):
        self.author = value

    def set_page_count(self, value):
        if value > 0:
            self.page_count = value

    def __str__(self):
        return (f" The book title is {self.title} by {self.author}. It has {self.page_count} pages.")
    
book1 = Book("Rainbow Fish", "John Smith", 30)

print(book1)

class Student: 
    def __init__(self, name, major, GPA):
        self.name = name
        self.major = major
        self.GPA = GPA

    def get_name(self):
        return self.name
    def get_major(self):
        return self.major
    def get_GPA(self):
        return self.GPA
    
    def set_name(self, value):
        self.name = value

    def set_major(self, value):
        self.major = value

    def set_GPA(self, value):
        if 0 <= value <= 4.0:
            self.GPA = value

    def introduce(self):
        return (f"Hi, I'm {self.name}. I'm studying {self.major}")
    
    def study_for_exam(self):
        old_GPA = self.GPA
        new_GPA = self.GPA + 0.2
        return (f" I'm hitting the books! My GPA increased from {old_GPA} to {new_GPA}.")
    
student1 = Student("James", "Computer Science", 3.5)

print(student1.introduce())
print(student1.study_for_exam())