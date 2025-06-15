package JAVA.src.swea.algorithmB;


import java.util.Scanner;

public class BinaryExpression {

    public static void main(String[] args)  {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();

        for (int t = 1; t <= T; t++) {
            int N = sc.nextInt();
            int M = sc.nextInt();

            int bit = (1 << N) - 1;     // 마지막 N개의 비트를 모두 1로 표현하기
            String result = ((M & bit) == bit) ? "ON" : "OFF";

            System.out.println("#" + t + " " + result);
        }
    }
}
