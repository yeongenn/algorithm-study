package JAVA.src.swea;

import java.util.Scanner;

public class Solution3 {

    // SWEA 1959. 두 개의 숫자열
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        

        for (int t = 1; t <= T; t++) {
            int max = 0;
            
            // A, B 배열 크기
            int A_size = sc.nextInt();
            int B_size = sc.nextInt();

            // 빈 배열 생성
            int[] arr_A = new int[A_size];
            int[] arr_B = new int[B_size];

            // A 배열
            for (int i = 0; i < arr_A.length; i++) {
                arr_A[i] = sc.nextInt();
            }

            // B 배열
            for (int i = 0; i < arr_B.length; i++) {
                arr_B[i] = sc.nextInt();

            }

            int[] arrL = {};
            int[] arrS = {};

            // 배열 길이 따라서 위치 구분
            if (arr_B.length > arr_A.length) {
                arrL = arr_B;
                arrS = arr_A;

            } else {
                arrL = arr_A;
                arrS = arr_B;
            }

            for (int i = 0; i <= arrL.length - arrS.length; i++) {
                int sum = 0;
                for (int j = 0; j < arrS.length; j++) {
                    sum += arrS[j] * arrL[i + j];
                    
                }
                if (max < sum) {
                    max = sum;
                }
                

            }

            System.out.println("#" + t + " " + max);
        }

    }

}
