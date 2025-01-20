package BOJ;

import java.util.Scanner;

public class Solution2480 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int A = sc.nextInt();
        int B = sc.nextInt();
        int C = sc.nextInt();

        int rewards = 0;

        /*
         * 같은 눈이 3개가 나오면 10,000원+(같은 눈)×1,000원의 상금
         * 같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)×100원의 상금
         * 모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)×100원의 상금
         */

        // if(A == B && B == C && C == A){
        // rewards = 10000 + (A * 1000);
        // } else if (A != B && B != C && C != A) {
        // int biggest =
        // rewards =
        // }

    }

}
