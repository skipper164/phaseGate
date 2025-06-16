contact_numb_list  = []
contact_1st_name_list = []
contact_last_name_list = []

option = 7
while (option != 0):
	print(f"""
	1. Add contact
	2. Remove contact
	3. Find contact by phone number
	4. Find contact by first name
	5. Find contact by last name
	6. Edit contact
	0. To end program
	""")

	option = int (input())
	count = 0
	match(option):
		case 1:
			while True:
				print("Add contact")
				contact_numb = input("enter contact number: ")
				contact_numb_list.append(contact_numb)
				contact_1st_name = input("contact first name: ")
				contact_1st_name_list.append(contact_1st_name)
				contact_last_name = input("contact last name: ")
				contact_last_name_list.append(contact_last_name)
				print()

				print(f"""
	Name: {contact_1st_name_list[count]}  {contact_last_name_list[count]}
	Address:
	Telephone: {contact_numb_list[count]}
	Email:
				""")

				count +=1
				add_more = input("your contact have been saved successfuly, do you want to add more? yes/no")
				if(add_more == "no"): break




		case 2: print("Remove contact")

		case 3: print("Find contact by phone number")

		case 4: print("Find contact by first name")

		case 5: print("Find contact by last name")

		case 6: print("Edit contact")

		case 0: print("goodbye")
	
		case _: print("enter a valid option ")

