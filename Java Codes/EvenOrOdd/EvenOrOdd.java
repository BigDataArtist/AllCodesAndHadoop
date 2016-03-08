public class EvenOrOdd{
	public static void main(String []args){
		int num = 20;
		boolean iseven = true;
			if (num %2!=0){
				iseven = false;
			}
			if (iseven==false){
				System.out.println(" this is odd number"+num);
			}
			else if(iseven==true){
				System.out.println(" this is even number"+num);
			}
			
		
	}
}