 import java.util.Scanner;

 public class GuessANumber{
 	public static void main(String []args){
 		int upperbound = 10;
 		int lowerbound = 1;
 		int secretNumber = (int)(Math.random()*upperbound+lowerbound);
 		boolean done = true;
 		Scanner number = new Scanner(System.in);
 		System.out.println(" the secretNumber is "+secretNumber);

 		while(done)
 		{
 			System.out.println(" enter the number");
 			int guess = number.nextInt();

 			if(guess == secretNumber){
 				System.out.println(" you have guesse the right number"+guess);
 				break;
 			}
 			else if(guess < secretNumber){
 				System.out.println(" guess too low"+ guess);
 			}
 			else {
 				System.out.println(" guess too high"+guess);

 				}
 		} 
 			System.out.println(" you owe me coke");
		



 	}
 }