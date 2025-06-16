const prompt = require("prompt-sync")();


/*console.log('
 1. Add contact
 2. Remove contact
 3. Find contact by phone number
 4. Find contact by first name
 5. Find contact by last name
 6. Edit contact
');*/ 

let option =prompt();

switch(option){
  case 1: { console.log("Add contact");
       };
	break;
  case 2: { console.log("Remove contact");

       };
	break;
 case 3: { console.log("Find contact by phone number");
       };
	break;
 case 4: { console.log("Find contact by first name");
       };
	break;
case 5: { console.log("Find contact by last name");
       };
	break;
 case 6: { console.log("Edit contact");
       };
	break;

 default: console.error("enter a valid option ");


}