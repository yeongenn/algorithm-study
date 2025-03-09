package JAVA.src.boj.etc;

import java.util.Scanner;

public class Solution25304 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int total = sc.nextInt();
        int T = sc.nextInt();

        int sum = 0;

        for (int i = 0; i < T; i++) {
            int price = sc.nextInt();
            int count = sc.nextInt();
            sum += price * count;

        }

        if (sum == total) {
            System.out.println("Yes");
        } else {
            System.out.println("No");
        }
    }

}
