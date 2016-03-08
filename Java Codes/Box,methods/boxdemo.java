/*
class box{
	double height;
	double width;
	double length;

public void volume(){
	System.out.println(" volume is ");
	System.out.println(height*width*length);
}
}
class boxdemo{
	public static void main(String []args){
		box mybox1 = new box();
		box mybox2 = new box();
		double vol1;
		double vol2;

		mybox1.height=10;
		mybox1.width=15;
		mybox1.length=10;

		mybox2.height=12;
		mybox2.width=13;
		mybox2.length=11;

		mybox1.volume();


		mybox2.volume();
	}
}
*/
/*
class box{
	double height;
	double width;
	double length;

public double volume(){
	return height*width*length;
}
}

class boxdemo{
	public static void main(String []args){
		box mybox1 = new box();
		box mybox2 = new box();
		double vol1;
		double vol2;

		mybox1.height=10;
		mybox1.width=15;
		mybox1.length=10;

		mybox2.height=12;
		mybox2.width=13;
		mybox2.length=11;

		vol1 = mybox1.volume();
	{
		System.out.println(" vol 1 is "+vol1);
	}



		vol2 = mybox2.volume();
	{
		System.out.println(" vol 2 is "+vol2);
	}
	}
}
*/

class box{
	double length;
	double width;
	double height;

public double volume(){
	return length*width*height;
}
public void setDim(double l,double w,double h){
    length = l;
	width = w;
	height=h;
}
}
class boxdemo{
	public static void main(String [] args){
		box mybox1 = new box();
		box mybox2 = new box();
		double vol1,vol2;

		mybox1.setDim(10,12,14);

		mybox2.setDim(11,13,14);
		

		vol1 = mybox1.volume();{
			System.out.println(" vol is "+ vol1);
		}
		vol2 = mybox2.volume();{
			System.out.println(" vol is "+vol2);
		}
		
	}
}

































