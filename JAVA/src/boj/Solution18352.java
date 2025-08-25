package JAVA.src.boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Solution18352 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());       // 정점 갯수
        int M = Integer.parseInt(st.nextToken());       // 간선 갯수
        int K = Integer.parseInt(st.nextToken());       // 거리 정보
        int X = Integer.parseInt(st.nextToken());       // 출발점

        boolean[] visited = new boolean[N + 1];
        int[] result = new int[N + 1];
        List<Node>[] list = new List[N + 1];

        // list 초기화
        for (int i = 1; i <= N; i++) {
            list[i] = new ArrayList<>();
            result[i] = Integer.MAX_VALUE;
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int A = Integer.parseInt(st.nextToken());       // 출발 간선
            int B = Integer.parseInt(st.nextToken());       // 도착 간선
            list[A].add(new Node(B, 1));            // 모든 도시 사이 거리는 1
            
        }

        // 다익스트라
        PriorityQueue<Node> pq = new PriorityQueue<>((o1, o2) -> o1.weight - o2.weight);
        result[X] = 0;
        pq.add(new Node(X, 0));
        while (!pq.isEmpty()) {
            Node now = pq.poll();
            if (!visited[now.end]) {
                visited[now.end] = true;
            }

            // 방문 가능 노드 순회
            for (int i = 0; i < list[now.end].size(); i++) {
                Node next = list[now.end].get(i);
                if (!visited[next.end] && now.weight + next.weight < result[next.end]) {
                    result[next.end] = now.weight + next.weight;

                    if (result[next.end] > K) { continue; }     // K 이상이면 패스

                    pq.add(new Node(next.end, result[next.end]));

                }
            }

        }

        // 최단 거리 K 경우 카운트, 출력
        int count = 0;
        for (int i = 1 ; i <= N ; i++) {
            if (result[i] == K) {
                count++;
                System.out.println(i);
            }
        }

        // 경로 없을 경우 -1 출력
        if (count == 0) System.out.println(-1);

    }
}
