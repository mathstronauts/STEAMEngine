# SEV Advanced - Class TEMPLATE

# initialize a student class
class student():
    def __init__(self, FirstName, LastName, Age, Grade):
        self.given_name = FirstName
        self.surname = LastName
        self.age = Age
        self.grade = Grade
        self.grades = []
        self.graduate = False
        
    def addGrade(self, Grade):
        # add Grade to grades list
    
    def getAverage(self):
        # calculate and return student's average grade
    
student1 = student('Kobe', 'Bryant', 15, 12)
student2 = student('LeBron', 'James', 13, 10)
        
