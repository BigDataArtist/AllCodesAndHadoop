public class twoD{
	public static void main(String []args){
	int i ,j;
	double matrix [][]={
	{0*1,0*2,0*3,0*4},
	{1*0,1*2,1*3,1*4},
	{2*1,2*2,2*3,2*4},
	{3*1,3*2,3*3,3*4},};

	for(i=0 ;i<4;i++){
		for(j=0;j<4;j++){
			System.out.print(matrix[i][j]+" ");
			} System.out.println();
	}
	}
}