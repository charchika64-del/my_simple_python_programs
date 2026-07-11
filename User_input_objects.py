class Student:
	def __init__(self,name,grade,age,hobby):
		self.name=name
		self.grade=grade
		self.age=age
		self.hobby=hobby
		
		
objects=[]
permission=input("Want to create objects?(y or n) ")
while permission=="y":
	num=int(input("Type 1 to create objects and type 2 to view: "))
	if num == 1:
		name=input("Enter name: ")
		grade=input("Enter grade: ")
		age=input("Enter age: ")
		hobby=input("Enter hobby: ")
		student_object=Student(name,grade,age,hobby)
		print("Object is created")
		objects.append(student_object.__dict__)
		permission=input("Continue?(y or n) ")
	else:
		if len(objects)==0:
			print("The item is not in list.")
			permission=input("Continue?(y or n) ")
		else:
			view=input("Enter object name: ")
			for item in objects:
				if item['name']==view:
					print(item)
			permission=input("Continue?(y or n) ")
				
