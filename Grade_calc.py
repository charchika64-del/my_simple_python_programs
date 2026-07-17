#This program takes student and score to get grade.
#It also saves the names and grades as a key-value pair in dictionary 
def give_grade(score):
	if score in range(90,101):
		return "Grade A"
	elif score in range(80,90):
		return "Grade B"
	elif score in range(60,80):
		return "Grade C"
	elif score in range(36,60):
		return "Grade D"
	else:
		return "Failed"	
	
permission = input("Want to get grades?(y or n) ")

list_of_grades={}		
while permission == "y":
	student=input("Enter student name: ")
	marks=int(input(f"Enter {student}'s marks: "))
	grade=give_grade(marks)
	print(f"{student} has got {grade}.")
	list_of_grades[student]=grade
	permission = input("Want to continue?(y or n) ")
else:
	print(list_of_grades)		

		
