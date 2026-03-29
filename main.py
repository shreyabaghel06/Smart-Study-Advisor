#main.py

import matplotlib
from advisor import analyzing_marks, suggesting_time, giving_advice 
from graph import show_graph

print("SMART STUDY ADVISOR")

#user/student name input
student_name = input("Enter your name: ")

#taking input
ECS= int(input("Enter your Electric cricuits and systems marks : ")) 
CHY = int(input("Enter your Intro to computational chemistry marks: "))
MAT = int(input("Enter your Calculus marks: "))
ETC = int(input("Enter your Effective Technical Communication marks: "))
CSE =  int(input("Enter your Intro to problem solving and programming marks: "))


subjects = ["Electric cricuits and systems ", "Intro to computational chemistry", "Calculus" , "Effective Technical Communication", "Intro to problem solving and programming"]
marks = [ECS, CHY , MAT , ETC , CSE]


#using loops
for sub, mark in zip(subjects, marks):
    print("\n" + sub + ":", mark)
    print("Performance:", analyzing_marks(mark))
    print("Study Hours:", suggesting_time(mark))
    print("Advice:", giving_advice(sub, mark))


# finding min and max marks
min_marks = min(marks)
max_marks = max(marks)

# getting index positions
weak_subject_index = marks.index(min_marks)
strong_subject_index = marks.index(max_marks)

# printing actual subject names instead of index 
print("\nWeakest subject:", subjects[weak_subject_index])
print("Strongest subject:", subjects[strong_subject_index])


# Show graph
show_graph(subjects, marks)

