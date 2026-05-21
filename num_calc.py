def sum(a,b):
	print(a + b)
def subtract(a,b):
	print(a - b)
def multiply(a,b):
	print(a * b)
def divide(a,b):
	print(a/b)
print("Calculator: Hey, i m here to perform some operations . If you want then write the numbers and after that  type 1 for addition, 2 for subtraction,3 for multiplication, 4 for division.")
n = int(input("Enter num1 "))
m = int(input("Enter num2 "))
l = int(input("Type the no. for operator "))
if l == 1:
	sum(n, m)
elif l == 2:
	subtract(n, m)
elif l == 3:
	multiply(n, m)
elif l == 4:
	divide(n, m)
else:
		print("Please do as instructed.")
	
