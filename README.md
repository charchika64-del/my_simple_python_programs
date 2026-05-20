# my-new-calculator
import math
def area_of_triangle():
	b = int(input("Enter base "))
	h = int(input("Enter height "))
	area = 1/2 * b * h
	print(f"The area of triangle is {area} sq. units")
#Functions are easy
def area_of_rhombus():
	v = int(input("Enter diagonal 1 "))
	p = int(input("Enter diagonal 2  "))
	Area = 1/2 * v * p
	print(f"The area of rhombus  is {Area} sq. units")
#Functions are easy
def area_of_circle():
	a = int(input("Enter radius "))
	b = math.pi * a * a
	print(f"The area of circle is {b} sq.units")
#Functions are easy
def hypotenuse():
	x = int(input("Enter base "))
	y = int(input("Enter perpendicular "))
	z = x * x + y * y
	d = math.sqrt(z)
	print(f"The hypotenuse is {d} units")

print("""System:Hello user . I can calculate area of rhombus, triangle, circle and i can also calculate hypotenuse.
            If you want area of triangle then type 1,2 for area of circle, 3 for rhombus , 4 for hypotenuse""")
permission=(input("Want to calculate(y or n): "))
while permission=="y":
	n = int(input("Enter the no. "))
	if n == 1:
		area_of_triangle()
	elif n == 2:
		area_of_circle()
	elif n == 3:
		area_of_rhombus()
	elif n == 4:
		hypotenuse()
	else:
		print("Please enter 1, 2, 3,4")
	permission=(input("Continue(y or n): "))
