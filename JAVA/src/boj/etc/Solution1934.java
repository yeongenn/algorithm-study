package JAVA.src.boj.etc;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution1934 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st = null;

        int T = Integer.parseInt(br.readLine());

        for (int i = 0; i < T; i++) {
            st = new StringTokenizer(br.readLine());
            int A = Integer.parseInt(st.nextToken());
            int B = Integer.parseInt(st.nextToken());

            sb.append((A * B) / getGcf(A, B)).append("\n");

        }

        System.out.println(sb.toString());
    }

    // static int getGcf(int a, int b) {
    //     int gcf = 0;
    //     for (int i = 1; i <= a; i++) {
    //         if (a % i == 0 && b % i == 0) {
    //             gcf = i;
    //         }
    //     }
    //     return gcf;
    // }

    // 재귀
    static int getGcf(int a, int b){
        if(b == 0) return a;
        return getGcf(b, a % b);
    }

}
