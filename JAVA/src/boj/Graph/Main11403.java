package JAVA.src.boj.Graph;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main11403 {

    /*
     * Floyd-warshall
     * 
     * 모든 최단 경로를 구하는 알고리즘
     * DP 활용
     * 가중 그래프에서도 가능
     * 음수 사이클 있는 경우에는 최단 경로 탐색 불가, 음수 사이클 여부 확인은 가능
     * 시간 복잡도는 O(N ^ 3)
     * 
     * 다익스트라의 경우
     * 하나의 정점에서 다른 모든 정점까지의 최단 거리를 구하는 알고리즘
     * 
     * 플로이드 워셜의 경우
     * 한번 실행하여 모든 노드 간 최단 경로 구할 수 있다
     * 
     * 알고리즘 구현
     * 1번부터 N(노드 수)번까지의 라운드
     * 라운드마다 각 경로에서 새로운 중간 노드 설정
     * 더 짧은 길이 선택해서 줄이는 과정 반복
     * 
     * for(int k = 1; k<= n; k++){
            for(int i = 1; i <= n; i++){
                for(int j = 1; j<=n; j++){
                    dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j]);
                }
            }
        }
     *
     * 각 라운드 별로 중간 노드가 될 노드 번호 k
     * 내부 이중 for 문에는 i, j를 통해 각 노드별 모든 거리 탐색
     * k를 중간 노드 삼을 때와 아닐 떄의 값을 비교해서 더 작은 값으로 업데이트
     * 
     * 
     * https://chanhuiseok.github.io/posts/algo-50/
     */


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = null;

        int N = Integer.parseInt(br.readLine());
        int[][] adj = new int[N][N];    // 배열 초기화

        for (int i = 0; i < N; i++){
            st = new StringTokenizer(br.readLine());    // 한 줄 단위로
            for (int j = 0; j < N; j++){
                adj[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        // Floyd-warshall
        for (int k = 0; k < N; k++){
            for (int i = 0; i < N; i++){
                for (int j = 0; j < N; j++){
                    if (adj[i][k] == 1 && adj[k][j] == 1) {
                        adj[i][j] = 1;
                    }
                }
            }
        }

        // 출력
        for (int i = 0; i < N; i++){
            for (int j = 0; j < N; j++){
                System.out.print(adj[i][j] + " ");
            }
            System.out.println();
        }

    }
    
}
