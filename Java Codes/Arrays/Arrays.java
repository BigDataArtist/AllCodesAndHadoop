/*
public class Arrays{
	public static void main(String [] args){
		int month_days[];
		month_days = new int[12];
		month_days[0]=31;
		month_days[1]=30;
		month_days[2]=31;
		month_days[3]=30;
		month_days[4]=31;
		month_days[5]=30;
		month_days[6]=31;
		month_days[7]=30;
		month_days[8]=31;
		month_days[9]=30;
		month_days[10]=31;
		month_days[11]=30;
		System.out.println(" april has"+month_days[3]+" in a year");


		int years[] = {1,2,3,4,5,6,7,8,9,10,11,12};
		System.out.println(" november is the "+years[10]+ "th month of the year ");

	}	
}
*/

public class Arrays{
	public static void main(String []args){
		double average[]={10.1,11.2,12.3,13.4,14.5};
		double secondArray[]={11.1,12.2,13.3,14.4,15.5};
		int i;
		double sum =0;
		double sum2 = 0;

		for (i=0;i<5;i++){
			sum = sum + average[i];
			sum2 = sum2 + secondArray[i];
			System.out.println(" avg is "+ sum/5 );
			System.out.println(" avg2 is "+sum2/5);

		}
			double total = sum+sum;
			System.out.println(" total of both the sum is "+total);
	
	}
}