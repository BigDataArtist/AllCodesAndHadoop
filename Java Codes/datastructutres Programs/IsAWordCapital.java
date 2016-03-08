import java.util.Scanner;

public class IsWordCapital{
	public static void main(String[]args){
		System.out.println(" Enter the character");
		Scanner input = new Scanner(System.in);
		String word = input.nextLine();

		boolean state = Character.isLowerCase(word.charAt(0));
		String result = state ?"is":"is not" ;

		System.out.println(word+result+"capitalzied");
	}
}
