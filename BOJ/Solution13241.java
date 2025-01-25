package BOJ;

import java.util.Scanner;

public class Solution13241 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        long A = sc.nextInt();
        long B = sc.nextInt();

        System.out.println((A * B) / getGcf(A, B));


    }

    // gcf
    static long getGcf(long a, long b){
        if (b == 0) {   // 종료 조건
            return a;
        }
        return getGcf(b, a % b);
    }
    
}
