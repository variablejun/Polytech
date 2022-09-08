import java.util.*;


public class string_SC {

	public static void main(String[] args) 
	{
		Scanner scanner = new Scanner(System.in);
		
		int intarr[] = new int[5];
		int myarr[] = intarr;
		int max = 0;
		System.out.println("양수 5개를 입력하세요");
		
		for(int i = 0; i < 5; i++) {
			myarr[i] = Math.abs(scanner.nextInt());
			if(myarr[i] > max) {
				max = myarr[i];
			}
		}
		System.out.println("가장 큰 수는 " + max + "입니다.");
		scanner.close();
		//System.out.println(arr[4]); 마지막 요소 배열 크기 -1
	}

}
