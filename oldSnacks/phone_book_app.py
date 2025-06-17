contact_numb_list  = []
contact_1st_name_list = []
contact_last_name_list = []

count = 0
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
	
	match(option):
		case 1:
			while True:
				print("Add contact")
				contact_numb = int (input("enter contact number: "))
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
				add_more = input("your contact have been saved successfuly, do you want to add more? yes/no: ")
				if(add_more == "no"): break




		case 2:
			while True:
				print("Remove contact")
				for loop in range(len(contact_numb_list)):
					print(f"{loop} {contact_1st_name_list[loop]} {contact_last_name_list[loop]} {contact_numb_list[loop]}")

				remove_contact = int (input("select a contact to remove: "))
				if(remove_contact > 0): remove_contact -=1
				del contact_numb_list[remove_contact]
				del contact_1st_name_list[remove_contact]
				del contact_last_name_list[remove_contact]
				print()
				print(f"{contact_1st_name_list[remove_contact]} {contact_last_name_list[remove_contact]} has been removed")
				end_remove = input("would you like to remove any other contact? (yes/no):  ")
				if (end_remove == "no"):break	
				




		case 3:
			while True:
				print("Find contact by phone number")
				for loop in range(len(contact_numb_list)):
					print(f"{contact_1st_name_list[loop]} {contact_last_name_list[loop]} {contact_numb_list[loop]}")
				
				print()
				search_cont = int (input("search contact by number: "))
				for loop in range(len(contact_numb_list)):
					if(search_cont == contact_numb_list[loop]): 
						print(f"{contact_1st_name_list[loop]} {contact_last_name_list[loop]} {contact_numb_list[loop]}")
				end_remove = input("would you like to go back to menu? (yes/no):  ")
				if (end_remove == "no"):break






		case 4:
			while True:
				print("Find contact by first name")
				for loop in range(len(contact_numb_list)):
					print(f"{contact_1st_name_list[loop]} {contact_last_name_list[loop]} {contact_numb_list[loop]}")
				
				print()
				search_cont = input("search contact by first name: ")
				for loop in range(len(contact_numb_list)):
					if(search_cont == contact_1st_name_list[loop]): 
						print(f"{contact_1st_name_list[loop]} {contact_last_name_list[loop]} {contact_numb_list[loop]}")
				end_remove = input("would you like to go back to menu? (yes/no):  ")
				if (end_remove == "no"):break

			


		case 5:
			while True:
				print("Find contact by last name")
				for loop in range(len(contact_numb_list)):
					print(f"{contact_1st_name_list[loop]} {contact_last_name_list[loop]} {contact_numb_list[loop]}")
				
				print()
				search_cont = input("search contact by last name: ")
				for loop in range(len(contact_numb_list)):
					if(search_cont == contact_last_name_list[loop]): 
						print(f"{contact_1st_name_list[loop]} {contact_last_name_list[loop]} {contact_numb_list[loop]}")
				end_remove = input("would you like to go back to menu? (yes/no):  ")
				if (end_remove == "no"):break






		case 6: print("Edit contact")

		case 0: print("goodbye")
	
		case _: print("enter a valid option ")

