from pygame import *

class Student:
    def __init__(self,name,courses,grades):
        self.name = name
        self.courses = courses
        self.grades = grades

def gpa(self):
    sum = 0
    for grade in self.grades:
        sum = sum + grade
        gpa = sum / len(self.grades)
        return gpa

def shared_classes(self, other):
    for courses in self.courses:
        for other_course in other.courses:
            if (courses == other_course):
                print("You share a course: " + courses) 
                return
    print("You do not share a course")


Jordan = Student("Jordan", ["Science", "Biology", "Physics"], [70, 75, 80])
Kobie = Student("Kobie", ["Gym", "Computer Science", "Math"], [90, 90, 100])
Mike = Student("Mike", ["Art", "ELA", "Science"], [100, 85, 90])