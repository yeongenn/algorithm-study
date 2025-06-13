package JAVA.src.swea.BackTracking;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Nqueen {

    static int count = 0;
    static int N;
    static int[] queens;
    static boolean[] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = null;

        int T = Integer.parseInt(br.readLine());

        for (int t = 0; t < T; t++){
            N = Integer.parseInt(br.readLine());
            queens = new int[N + 1];
            visited = new boolean[N + 1];     // 마킹용

            play(0);        // 
        }

    }

    static void play(int n) {
        if (n == N) {
            count++;
            return;
        }

        // n번째 행에 놓을 수 있는 열 찾기
        for (int j = 0; j < N; j++){
            if (visited[j]) {
                continue;
            }

            boolean isValid = true;
            for (int k = 0; k < N; k++){
                if (Math.abs(k - n) == Math.abs(queens[k] - j)) {
                    isValid = false;
                    break;
                }
            }

            if (isValid) {
                queens[n] = j;      // 현재 행(j)에 놓을 수 있다
                visited[j] = true;  // 마킹
                play(n + 1);         // 다음 행에 퀸 놓으러 가기
                visited[j] = false; // 언마킹
            }

        }
    }
    
}
