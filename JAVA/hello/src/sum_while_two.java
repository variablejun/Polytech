import java.util.*;
public class sum_while_two {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		
		int num1 = 0;
		int num2 = 0;
		int sum = 0;
		int count = 0;
		
		while(true) {
			count++;
			System.out.println( count + " 번째 연산");
			
			System.out.print("첫번쨰 숫자를 입력하세요 : ");
			num1 = scanner.nextInt();
			System.out.print("두번쨰 숫자를 입력하세요 : ");
			num2 = scanner.nextInt();	
			
			
			sum = num1 + num2;
			System.out.println(num1 + " + " + num2 + " = "  + sum);
			sum = 0;
			
			System.out.println("=====================");
			if(count == 10) {
				System.out.println("종료");
				break;				
			}			
		}	
	}
}