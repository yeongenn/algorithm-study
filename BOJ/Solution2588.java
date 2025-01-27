package BOJ;

import java.util.Scanner;

public class Solution2588 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int A = sc.nextInt();
        int B = sc.nextInt();
        // String B = sc.next();

        // int sum = 0;

        // (세 자리) * (세 자리)
        // for(int i = 0; i < 3; i++){
        //     int num = B % 10;
        //     B /= 10;
        //     int m = num * ((int) (Math.pow((double) 10, (double) i)));
        //     System.out.println((A * m) / ((int) (Math.pow((double) 10, (double) i))));
        //     sum += (A * m);
        // }

        // 1. B를 String으로 받아 charAt 사용
        // System.out.println(A * (B.charAt(2) - '0'));
        // System.out.println(A * (B.charAt(1) - '0'));
        // System.out.println(A * (B.charAt(0) - '0'));
        // System.out.println(A * Integer.parseInt(B));

        // 2. <- 이건 자릿수가 정해져있어서 가능한 방법
        System.out.println(A * (B % 10));   //  1
        System.out.println(A * (B % 100 / 10)); //  10
        System.out.println(A * (B % 100));  // 100
        System.out.println(A * B);

        // 3. BufferedReader 사용
        // 생략
        


        // System.out.println(sum);
        
        
    }

}
