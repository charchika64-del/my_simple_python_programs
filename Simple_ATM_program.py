#This is a program which works like ATM and it asks to deposit,to withdraw,
# to view current money
#Type 8850 in credit card no.

n = input("Enter your credit card no.")
credit_no = "8850"
while n != credit_no:
	print("That is invalid.")
	n = input("Enter your credit card no.")
else:
	print()
print("""Welcome,do as given-
           Type 1 to check balance
           Type 2 to exit 
           Type 3 to deposit
           Type 4 to withdraw""")
balance = 1000
s = int(input("Enter digit "))
while s != 2:
	if s == 3:
		t = int(input("Deposit amount: "))
		balance = balance + t
		print("Your balance is ₹",balance)
	elif s == 4:
		d = int(input("Withdraw amount:"))
		balance = balance - d
		print("Your balance is ₹",balance)
	elif s == 1:
		print("Your balance is ₹",balance)
	else:
		break
	print("Want to continue?")
	s = int(input("Enter digit "))
