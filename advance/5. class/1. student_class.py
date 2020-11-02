# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 22:52:04 2020

@author: JZST6G
"""

class student():
    def __init__(self,FirstName, LastName, Age, Grade):
        self.given_name = FirstName
        self.surname = LastName
        self.age = Age
        self.grade = Grade
        self.grades = []
        self.graduate = False
        
    def addGrade(self, Grade):
        self.grades.append(Grade)
    
    def getAverage(self):
        average = sum(self.grades)/len(self.grades)
        return average
    
student1 = student('Kobe', 'Bryant', 15, 12)
student2 = student('LeBron', 'James', 13, 10)
        
