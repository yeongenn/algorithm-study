package JAVA.src.boj.Graph;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main11404 {

    /*
     * !! caution !!
     * 
     * 입력받을 때 작은 비용으로 갱신할 것
     * 갈 수 없는 곳 INF로 받았다가 출력할 때 0으로 바꾸기!
     * 
     * 
     */

     static final int INF = 10000001;   // 최댓값 + 1

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = null;
        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(br.readLine()); // 노드 수
        int M = Integer.parseInt(br.readLine()); // 버스 수
        int[][] adj = new int[N + 1][N + 1];

        // 초기 설정
        for (int i = 1; i <= N; i++) {
            for (int j = 1; j <= N; j++) {
                adj[i][j] = INF;

                if (i == j) {
                    adj[i][j] = 0;  // 시작 == 도착은 없다고 했으니까 여긴 0으로 고정
                }
            }
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine()); // 출발, 도착, 비용
            int depart = Integer.parseInt(st.nextToken());
            int arrival = Integer.parseInt(st.nextToken());
            int cost = Integer.parseInt(st.nextToken());

            adj[depart][arrival] = Math.min(cost, adj[depart][arrival]);
        }

        for (int k = 1; k <= N; k++) {
            for (int i = 1; i <= N; i++) {
                for (int j = 1; j <= N; j++) {
                    adj[i][j] = Math.min(adj[i][j], adj[i][k] + adj[k][j]);
                }
            }
        }

        // 출력
        for (int i = 1; i <= N; i++) {
            for (int j = 1; j <= N; j++) {
                if (adj[i][j] == INF) {
                    adj[i][j] = 0;      // 변환
                }

                sb.append(adj[i][j] + " ");
            }
            sb.append("\n");
        }

        System.out.println(sb.toString());

    }

}
