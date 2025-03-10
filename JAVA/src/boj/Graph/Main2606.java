package JAVA.src.boj.Graph;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main2606 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = null;

        int N = Integer.parseInt(br.readLine());    // 컴퓨터 수
        int M = Integer.parseInt(br.readLine());    // 간선 수
        int[][] computers = new int[N + 1][N + 1];
        for (int i = 0; i < M; i++){
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            computers[a][b] = 1;
            computers[b][a] = 1;    // 양방향
        }

        
        // floyd-warshall
        for (int k = 1; k <= N; k++){
            for (int i = 1; i <= N; i++){
                for (int j = 1; j <= N; j++){
                    if (i == j) {
                       continue; 
                    }

                    if (computers[i][k] == 1 && computers[k][j] == 1) {
                        computers[i][j] = 1;
                    }
                }
            }
        }
        
        // // 확인용
        // for (int i = 1; i <= N; i++){
        //     for (int j = 1; j <= N; j++){
        //         System.out.print(computers[i][j] + " ");
        //     }
        //     System.out.println();
        // }
        System.out.println(Arrays.deepToString(computers));     // 2차원 배열 for문 없이 확인하기

        // 출력
        int count = 0;      // 감연된 컴퓨터 수
        for (int j = 1; j <= N; j++){
            count += computers[1][j];
        }

        System.out.println(count);
    }
    
}
