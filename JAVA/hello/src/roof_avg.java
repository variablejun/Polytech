import java.util.*;

public class roof_avg {

	public static void main(String[] args) {
		System.out.println("숫자를 입력하세요 : ");
		Scanner scanner = new Scanner(System.in);
		int num = 0;
		int count = 0;
		int sum = 0;
		
		while(true) {
			num = scanner.nextInt();	
			if(num == -1) {
				System.out.println("종료합니다.");
				break;
			}
			sum = sum + num;
			count++;
			System.out.println("입력된 정수 개수 : "+ count);
			System.out.println("입력된 정수의 합 : "+ sum);
			System.out.println("입력 정수 평균 : " + (double)sum / count );
			System.out.println("========================");
			System.out.println("숫자를 입력하세요 : ");
			
		
		}
	}

}
