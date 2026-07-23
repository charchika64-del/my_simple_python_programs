#This program creates report card by taking name, class, subject name, 
#and marks obtained in each subject.
def subject_and_marks(dictionary):
    subject=input("Enter subject name: ")
    marks=int(input(f"Enter {subject}'s marks: "))
    dictionary[subject]=marks
   
dict_of_marks = {}  
student=(input("Enter name of student: "))
grade=input("Enter class: ")
permission= input("Want to calculate?(y or n) ")
max=int(input("Enter maximum marks: "))
while permission=="y":
    subject_and_marks(dict_of_marks)
    permission= input("Continue?(y or n) ")
else:
         print(f" ------------------------------------------------------------REPORT CARD------------------------------------------------------------")
         print("Name:", student)
         print("Class", grade)
         total=0
         print()
         print(" Subject   Marks  Maximum Marks")
         for value in dict_of_marks.values():
             total=value+total
         for key, value in dict_of_marks.items():
             print(f"{key} | {value} |  {max}")

            
print("Total",total)

