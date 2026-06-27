#A Text-Based Inventory Manager: Write a program that uses functions 
# to add items to an inventory list, remove them, or view the current stock.
inventory = []
print("Type 1 to add items, 2 to remove items and 3 to view list")
check = input("Want to add items?(y or n): ")
while check == "y":
	p = (input("Enter the number "))
	if p=="1":
		add_item = input("Which item you want to add? ")
		inventory.append(add_item)
	elif p=="2":
		remove_item=input("Which item you want to remove? ")
		inventory.remove(remove_item)
	else:
		print(inventory)
	check = input("Continue ?(y or n): ")
	
