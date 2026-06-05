num = int(input("Enter number  "))
start = int(input("Enter start value of range  "))
end = int(input("Enter end value of range  "))
for i in range(start,end+1):
	if num%i == 0:
		print(i)
