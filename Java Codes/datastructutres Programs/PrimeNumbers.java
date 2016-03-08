public class PrimeNumbers{
	 public static void main(String[] args) 
	 {
	 	int num = 14;
	 	boolean isprime = true;

	 	for(int i = 2;i<num;i++)
	 	{
	 		if (num%i==0)
	 		{
	 			isprime = false;
	 			
	 			
	 		}
	 	}
	 	if (isprime==false)
	 	{
	 			System.out.println(num + "is a prime munber");
	 	}
	 	else if (isprime==true)
	 	{

				System.out.println(" number is prime number"+num);
	 	}
	 }
}
