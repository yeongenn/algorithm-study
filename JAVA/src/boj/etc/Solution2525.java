package JAVA.src.boj.etc;

import java.util.Scanner;

public class Solution2525 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
 
        int A = sc.nextInt();
        int B = sc.nextInt();
        int C = sc.nextInt();

        // 시간 분단위로 통일
        int start = A * 60 + B;
        int end = start + C;

        // HH MM으로 환산
        int hour = (end / 60) % 24;
        int minute = end % 60;

        System.out.println(hour + " " + minute);
    }

}
