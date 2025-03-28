package JAVA.src.swea.Greedy;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.StringTokenizer;

public class MeetingRoom {

    static int N;
    static int Q;

    // 시간 초과
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = null;
        int T = Integer.parseInt(br.readLine());
        for (int i = 0; i < T; i++){
            st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken());
            Q = Integer.parseInt(st.nextToken());

            int[][] schedules = new int[N][2];
            for (int n = 0; n < N; n++){
                st = new StringTokenizer(br.readLine());
                int s = Integer.parseInt(st.nextToken());
                int e = Integer.parseInt(st.nextToken());
                schedules[n][0] = s;
                schedules[n][1] = e;
            }
            // System.out.println(Arrays.deepToString(schedules));
            Arrays.sort(schedules, Comparator.comparingInt((int[] x) -> x[1]).thenComparingInt(x -> x[0]));

            int answer = 0;     // q * count 누적합
            for (int q = 0; q < Q; q++){
                st = new StringTokenizer(br.readLine());
                int l = Integer.parseInt(st.nextToken());
                int r = Integer.parseInt(st.nextToken());

                int count = 0;
                int prev = 0;
                for (int n = 0; n < N; n++){
                    int s = schedules[n][0];
                    int e = schedules[n][1];
                    if (s >= l && e <= r) {
                        if (count == 0) {
                            prev = e;   // 이전 회의 종료시간 갱신
                            count++;
                        } else {
                            if (s >= prev) {
                                count++;
                                prev = e;
                            }
                        }
                    }
                    
                }
                answer += ((q + 1) * count);

            }
            System.out.println("#" + (i + 1) + " " + answer);
        }
    }
    
}