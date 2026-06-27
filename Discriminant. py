import math
a = int(input("Enter a : "))
b = int(input("Enter b : "))
c = int(input("Enter c : "))

d=b**2-4*a*c

if d<0:
	print(f"Discriminant:{d} (imaginary roots)")
	print(f"Alpha --> ({-1*b} + i√{abs(d)}) / {2*a}")
	print(f"Beta  --> ({-1*b} - i√{abs(d)}) / {2*a}")

else:
	print(f"Discriminant:{d} (real roots)")
	D=math.isqrt(d)
	if d!=D*D:
		print("irrational roots")
		print(f"Alpha --> ({-1*b} + √{d})/{2*a}")
		print(f"Beta --> ({-1*b} - √{d})/{2*a}")
	else:
		print("rational roots")
		print(f"Alpha --> {(-1*b + math.sqrt(d))/2*a}")
		print(f"Beta --> {(-1*b - math.sqrt(d))/2*a}")


