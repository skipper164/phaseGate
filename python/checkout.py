item_list = []
numb_of_item_list = []
price_list = []
total_list = []
count = 0
sub_total = 0

c_name = input("enter customer's name?: ")

while True:
	item = input("what did the user buy?: ")
	item_list.append(item)

	numb_of_item = int(input("how many pieces?: "))
	numb_of_item_list.append(numb_of_item)

	price = int(input("how much per unit?: "))
	price_list.append(price)

	loop = input("do you want to continue?: ")


	total =  price * numb_of_item
	total_list.append(total) 
	sub_total += total
	count +=1 
	
	if (loop == "no"): break


cashier_name = input("what is your name: ")
discount = int(input("how much discount will he get?: "))








discount = (discount / 100) * sub_total
vat = 0.175 * sub_total 
bill_total = (sub_total + vat) - discount










print(f"""
MAIN BRANCH
LOCATION: 312, ALBERT MACUALAY WAY, SABO YABA, LAGOS.
TELL: 09064921852
Date: 12-jul-2025 10:50:24 am
cashier:{cashier_name} 
customer name:{c_name}
=====================================================
		ITEM	QTY	PRICE	   TOTAL(NGN)
------------------------------------------------------
""")

for loop in range(count):
	print(f"		{item_list[loop]}	{numb_of_item_list[loop]}	{price_list[loop]}		{total_list[loop]}")


print(f"""
-------------------------------------------------------
			sub total:	{sub_total}
			 discount:	{discount}
		       vat @17.5%: 	{vat}
=======================================================
		       Bill total:	{bill_total}
=======================================================
THIS IS NOT A RECEIPT KINDLY PAY {bill_total} 
=======================================================			
""")

payment = int(input("how much did the customer give you?: "))

ballance = payment - bill_total

print(f"""
MAIN BRANCH
LOCATION: 312, ALBERT MACUALAY WAY, SABO YABA, LAGOS.
TELL: 09064921852
Date: 12-jul-2025 10:50:24 am
cashier:{cashier_name} 
customer name:{c_name}
=====================================================
		ITEM	QTY	PRICE	    TOTAL(NGN)
------------------------------------------------------
	 
""")

for loop in range(count):
	print(f"		{item_list[loop]}	{numb_of_item_list[loop]}	{price_list[loop]}		{total_list[loop]}")


print(f"""


-------------------------------------------------------
			sub total:	{sub_total}
			 discount:	{discount}
		       vat @17.5%: 	{vat}
=======================================================
		       Bill total:	{bill_total}
		      Amount paid:	{payment}
			 Ballance:	{ballance}
=======================================================
THANK YOU FOR YOUR PATRONAGE! 
=======================================================			
""")






