const input = require("prompt-sync")();

let itemList = [];
let numbOfItemList = [];
let priceList = [];
let totalList = [];
let count = 0;
let subTotal = 0;

cName = input("enter customer's name?: ");

while (true){
	item = input("what did the user buy?: ");
	itemList.push(item);

	numbOfItem = input("how many pieces?: ");
	numbOfItemList.push(numbOfItem);

	price = input("how much per unit?: ");
	priceList.push(price);

	loop = input("do you want to continue?: ");


	let total =  price * numbOfItem;
	totalList.push(total); 
	subTotal += total;
	count +=1; 
	
	if (loop == "no") break;
};

cashierName = input("what is your name: ");
discount = input("how much discount will he get?: ");






discount = (discount / 100) * subTotal;
let vat = 0.175 * subTotal; 
let billTotal = (subTotal + vat) - discount;




/*

console.log('
MAIN BRANCH
LOCATION: 312, ALBERT MACUALAY WAY, SABO YABA, LAGOS.
TELL: 09064921852
Date: 12-jul-2025 10:50:24 am
cashier:{cashierName} 
customer name:{cName}
=====================================================
		ITEM	QTY	PRICE	   TOTAL(NGN)
------------------------------------------------------
'); */

for (let loop = 0; loop < itemList.length; loop++){
	console.log('		${itemList[loop]}	${numbOfItemList[loop]}	${priceList[loop]}		${totalList[loop]}');
};

/*console.log('
-------------------------------------------------------
			sub total:	{subTotal}
			 discount:	{discount}
		       vat @17.5%: 	{vat}
=======================================================
		       Bill total:	{billTotal}
=======================================================
THIS IS NOT A RECEIPT KINDLY PAY {billTotal} 
=======================================================			
');

payment = input("how much did the customer give you?: ");

let ballance = payment - billTotal;

console.log('
MAIN BRANCH
LOCATION: 312, ALBERT MACUALAY WAY, SABO YABA, LAGOS.
TELL: 09064921852
Date: 12-jul-2025 10:50:24 am
cashier:{cashierName} 
customer name:{cName}
=====================================================
		ITEM	QTY	PRICE	    TOTAL(NGN)
------------------------------------------------------
	 
');

for loop in count{
	console.log("		{itemList[loop]}	{numbOfItemList[loop]}	{priceList[loop]}		{totalList[loop]}")

};
console.log('


-------------------------------------------------------
			sub total:	{subTotal}
			 discount:	{discount}
		       vat @17.5%: 	{vat}
=======================================================
		       Bill total:	{billTotal}
		      Amount paid:	{payment}
			 Ballance:	{ballance}
=======================================================
THANK YOU FOR YOUR PATRONAGE! 
=======================================================			
');


*/



