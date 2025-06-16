const prompt = require("prompt-sync")();

let creditCard = prompt("enter your credit card number: ");

let convertCard = [...creditCard].map(Number);

let sum = 0;
let sum2 = 0;
let loop2 = 0;
sumTotal = 0;
for(let loop = 0; loop < convertCard.length; loop++){
	
	let checkPoint = convertCard[loop] * 2;
	sum += checkPoint;
	if (checkPoint > 9) sum -= 9;
	loop2 += 1;
	sum2 += convertCard[loop2];
	loop+=1;

	sumTotal = sum + sum2;
}
//console.log(sumTotal);
let cardType = "null";
let status = "invalid";

if (convertCard.length >= 13 && convertCard.length <= 16 ){
	if(convertCard[0] == 4){ cardType = "visa card";
		if(sumTotal % 10 == 0)status = "valid";
	}
	if(convertCard[0] == 5){ cardType = "master card";
		if(sumTotal % 10 == 0)status = "valid";
	}
	if(convertCard[0] == 3 && convertCard[1] == 7){ cardType = "american express"
		if(sumTotal % 10 == 0)status = "valid";
	}
	if(convertCard[0] == 6){ cardType = "discovery card";
		if(sumTotal % 10 == 0)status = "valid";
	}
console.log();
console.log("credit card type: " + cardType);
console.log("credit card number: "+ creditCard);
console.log("credit card length: " + convertCard.length);
console.log("credit card validity status: "+ status);

}

else console.log("invalid card length");


