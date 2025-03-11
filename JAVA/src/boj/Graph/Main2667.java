package JAVA.src.boj.Graph;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main2667 {

    // static 
    static ArrayList<Integer> arr;      // 단지별 집 수 관리
    static int[][] houses;
    static boolean[][] visited;
    static int n;

    // // BFS 좌표 관리를 클래스로 하고 싶으면~
    // static class Location {
    //     int r;
    //     int c;

    //     public Location(int r, int c) {
    //         this.r = r;
    //         this.c = c;
    //     }
    // }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = null;

        n = Integer.parseInt(br.readLine());
        houses = new int[n][n];
        visited = new boolean[n][n];    // 마킹용
        int count = 0;                      // 단지 수
        arr = new ArrayList<>();

        for (int i = 0; i < n; i++){
            String[] strArr = br.readLine().split("");      // 연속된 숫자 분리해서 배열에 담기
            for (int j = 0; j < n; j++){
                houses[i][j] = Integer.parseInt(strArr[j]);
            }
        }

        // // 확인용
        // System.out.println(Arrays.deepToString(houses));

        for (int i = 0; i < n; i++){
            for (int j = 0; j < n; j++){
                if (!visited[i][j] && houses[i][j] == 1){
                    int temp = connected_house(i, j);
                    // System.out.println(temp);
                    arr.add(temp);

                    count++;
                }
            }
        }

        // 출력
        Collections.sort(arr);  // 단지 내 집 수 정렬
        System.out.println(count);
        for (int house : arr){
            System.out.println(house);
        }

    }

    // 

    // BFS
    static int connected_house(int y, int x){
        int house_count = 0;      // 단지 내 집 수

        // delta
        int[] dy = {-1, 1, 0, 0};
        int[] dx = {0, 0, -1, 1};

        Queue<int[]> q = new LinkedList<>();    // 좌표 배열 관리, 따로 클래스 만들어서 관리해도 가능
        q.add(new int[]{y, x});
        visited[y][x] = true;
        house_count++;

        while (!q.isEmpty()) {
            int[] now = q.poll();

            for (int d = 0; d < 4; d++){
                int ny = now[0] + dy[d];
                int nx = now[1] + dx[d];

                if (ny >= 0 && ny < n && nx >= 0 && nx < n && !visited[ny][nx] && houses[ny][nx] == 1) {
                    q.add(new int[]{ny, nx});
                    visited[ny][nx] = true;
                    house_count++;
                }
            }
        }
        
        // arr.add(house_count);
        return house_count;
    }
    
}
