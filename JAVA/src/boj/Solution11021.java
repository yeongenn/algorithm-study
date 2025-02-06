package JAVA.src.boj;

import java.util.Scanner;

public class Solution11021 {

    // A + B - (7), A + B - (8)
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();

        for(int i = 0; i < T; i++){
            int a = sc.nextInt();
            int b = sc.nextInt();
            // System.out.printf("Case #%d: %d%n", i + 1, a + b);   // (7)
            System.out.printf("Case #%d: %d + %d = %d%n", i + 1, a, b, a + b);  // (8)
        }
    
    }
    
}
