public class conditional{
	public static void main(String []args){
		int month = 9;
		String season;
		if (month ==12|| month==11|| month==10)
			season = " winter";
		else if(month == 9|| month== 8|| month==7)
			season=" fall";
		else if(month ==6|| month==5|| month==4)
			season="summer";
		else if (month ==3|| month==2|| month==1)
			season="spring";
		else
			season ="Bogus month";

		System.out.println(" april is the "+season+"");
	}
}