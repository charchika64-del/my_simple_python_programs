#Hey, thus program can filter students on the basis of their property and 
#value given by user.
#The students are Rahul,Riya,Vikram,Kamal,Siya,Champa
class Student:
	def __init__(self,name,grade,roll_no,age):
		self.name=name
		self.grade=grade
		self.roll_no=roll_no
		self.age=age
#name,grade,roll_no.,age		
Rahul=Student("Rahul",4,21,10)
Riya=Student("Riya",9,35,14)
Vikram=Student("Vikram",3,56,9)
Kamal=Student("Kamal",10,44,16)
Siya=Student("Siya",2,23,8)
Champa=Student("Champa",12,48,18)
  
students=[Rahul,Riya,Vikram,Kamal,Siya,Champa]
 
property=input("Enter class property: ")
property=property.lower()
value = int(input("Enter the value: "))
print(f"""Type 1 to get students greater than {value} in {property}
              Type 2 to get students greater than and equal to {value} in {property}
              Type 3 to get students equal to {value} in {property}
              Type 4 to get students smaller than {value} in {property}
              Type 5 to get students smaller than and equal to {value} in {property}""")
num=int(input("Enter the number: "))
 
# CHANGED: Replaced student.property with getattr(student, property)
# CHANGED: Replaced print(student) with print(student.name)
if num==1:
	for student in students:
		if getattr(student, property)>value:
			print(student.name)
elif num==2:
	for student in students:
		if getattr(student, property)>=value:
			print(student.name)
elif num==3:
	for student in students:
		if getattr(student, property)==value:
			print(student.name)
elif num==4:
	for student in students:
		if getattr(student, property)<value:
			print(student.name)
else:
	for student in students:
		if getattr(student, property)<=value:
			print(student.name)
