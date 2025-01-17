package BOJ;

import java.util.Scanner;

public class Solution2588 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int A = sc.nextInt();
        int B = sc.nextInt();


        // 숫자열 길이
        // (int) (Math.log10(num) + 1)
        int T = (int) (Math.log10(B) + 1);
        int sum = 0;
        for(int i = 1 ; i <= T ; i++){
            int n = A * (B%10);
            System.out.println(n);
            sum += n;
            B = B/10;      
        };
        
        System.out.println(sum);
        
        
    }

}
