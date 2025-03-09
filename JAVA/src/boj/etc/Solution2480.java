package JAVA.src.boj.etc;

import java.util.Scanner;

public class Solution2480 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int A = sc.nextInt();
        int B = sc.nextInt();
        int C = sc.nextInt();

        int rewards = 0;

        if (A == B && B == C) {
            rewards = 10000 + A * 1000;
        } else if (A == B || A == C) {
            rewards = 1000 + A * 100;
        } else if (B == C) {
            rewards = 1000 + B * 100;
        } else {    // 주사위 눈 모두 다를 경우
            int m = Math.max(A, Math.max(B, C));
            rewards = m * 100;
        }

        System.out.println(rewards);
    }

}
