package JAVA.src.boj.Graph;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main2667 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = null;

        int N = Integer.parseInt(br.readLine());
        int[][] houses = new int[N][N];
        int[][] visited = new int[N][N];    // 마킹용
        int count = 0;                      // 단지 수
        for (int i = 0; i < N; i++){
            String[] strArr = br.readLine().split("");      // 연속된 숫자 분리해서 배열에 담기
            for (int j = 0; j < N; j++){
                houses[i][j] = Integer.parseInt(strArr[j]);
            }
        }

        // 확인용
        System.out.println(Arrays.deepToString(houses));

        for (int i = 0; i < N; i++){
            for (int j = 0; j < N; j++){
                if (visited[i][j] == 0){
                    int temp = connected_house(i, j);
                    System.out.println(temp);

                    count++;
                }
            }
        }
    }

    // BFS
    static int connected_house(int y, int x){
        int house_count = 0;      // 단지 내 집 수

        Queue<int[]> q = new LinkedList<>();    // 좌표 배열 관리
        
        return house_count;
    }
    
}
