import java.util.Scanner;
public class PhoneBookApp {
public static void main(String...arg){
Scanner input = new Scanner(System.in);

int option = 7;
while (option != 0){
System.out.println("""
 1. Add contact
 2. Remove contact
 3. Find contact by phone number
 4. Find contact by first name
 5. Find contact by last name
 6. Edit contact
 0. To end program
""");

option = input.nextInt();

switch(option){
  case 1: { System.out.println("Add contact");
	
       };
	break;
  case 2: { System.out.println("Remove contact");

       };
	break;
 case 3: { System.out.println("Find contact by phone number");
       };
	break;
 case 4: { System.out.println("Find contact by first name");
       };
	break;
case 5: { System.out.println("Find contact by last name");
       };
	break;
 case 6: { System.out.println("Edit contact");
       };
	break;
 case 0: System.out.println("goodbye");break;

 default: System.out.println("enter a valid option ");

}


}






}




}