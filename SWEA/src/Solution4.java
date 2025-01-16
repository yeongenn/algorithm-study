import java.util.Scanner;

public class Solution4 {

    // SWEA 2058. 자릿수 더하기
    public static void main(String[] args) {
        
        int answer = 0;
        
		Scanner sc = new Scanner(System.in);
		int num = sc.nextInt();
		
        // 숫자열 끊기
        while (num > 0) {
        	int a = num % 10;
            answer += a;
            num /= 10;
        }
        
        System.out.println(answer);
    }
    
}
