
public class roof_while {

	public static void main(String[] args) {
		int i = 1;
		int sum = 0;
		while(i <= 10) {
			if(i <= 9) {
				System.out.print(i + " + ");
			}else {
				System.out.print(i + " = ");
			}
			sum = sum + i;
			i++;
			
		}
		System.out.println(sum);

	}

}
