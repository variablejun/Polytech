
public class roof_sum {

	public static void main(String[] args) {
		int sum = 0;
		
		for(int i = 1;i<=10;i++) {
			if(i <= 9) {
				System.out.print(i + " + ");
			}else {
				System.out.print(i + " = ");
			}
			
			sum = sum + i;
		}
		
		System.out.println(sum);
	}

}
