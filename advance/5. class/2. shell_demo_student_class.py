Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: W:\My Documents\Mathstronauts\repos\python_workshops\steam engine\advance\5. class\student_class.py 
>>> student1.given_name
'Kobe'
>>> student2.given_name
'LeBron'
>>> student1.age
15
>>> student2.age
13
>>> student1.grades
[]
>>> student2.grades
[]
>>> student1.graduate
False
>>> student2.graduate
False
>>> student1.addGrade(98) #student 1 got 98 in Math
>>> student1.grades
[98]
>>> student2.addGrade(63) #student 2 got 63 in Math
>>> student2.grades
[63]
>>> student1.addGrade(87) #student 1 got 87 in History
>>> student2.addGrade(70) #student 2 got 70 in History
>>> student1.addGrade(100)#student 1 got 100 in Gym
>>> student2.addGrade(60) #student 2 got 60 in Gym
>>> student1.grades
[98, 87, 100]
>>> student2.grades
[63, 70, 60]
>>> student1.getAverage()
95.0
>>> student2.getAverage()
64.33333333333333
>>> student1.age = 16
>>> student1.graduate = True #Kobe graduated
>>> student2.age = 14
>>> student2.grade = 11
>>> student1.age
16
>>> student2.age
14
>>> student1.graduate
True
>>> student2.graduate
False
>>> student2.grade
11
>>> 
