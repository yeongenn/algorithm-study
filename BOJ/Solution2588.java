package BOJ;

import java.util.Scanner;

public class Solution2588 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int A = sc.nextInt();
        int B = sc.nextInt();

        int sum = 0;

        // (세 자리) * (세 자리)
        for(int i = 0; i < 3; i++){
            int num = B % 10;
            B /= 10;
            int m = num * ((int) (Math.pow((double) 10, (double) i)));
            System.out.println((A * m) / ((int) (Math.pow((double) 10, (double) i))));
            sum += (A * m);
        }

        System.out.println(sum);
        
        
    }

}
