package JAVA.src.boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

class Node {
    int end;
    int weight;

    public Node(int end, int weight) {
        this.end = end;
        this.weight = weight;
    }
}

public class Solution1753 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int V = Integer.parseInt(st.nextToken());
        int E = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(br.readLine());

        boolean[] visited = new boolean[V + 1];     // 방문 처리 배열
        int[] result = new int[V + 1];              // 최단 경로 저장
        List<Node>[] list =  new List[V + 1];   // 간선 정보 저장

        // list 초기화
        for (int i = 1; i <= V; i++) {
            list[i] = new ArrayList<>();
            result[i] = Integer.MAX_VALUE;
        }

        // 간선 정보 저장
        for (int i = 1; i <= E; i++){
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());
            list[u].add(new Node(v, w));
        }
        
        // 다익스트라
        PriorityQueue<Node> queue = new PriorityQueue<>((o1, o2) -> o1.weight - o2.weight);
        result[K] = 0;      // 시작점 가중치는 0
        queue.add(new Node(K, 0));
        while (!queue.isEmpty()){
            Node now = queue.poll();
            if (!visited[now.end]) {
                visited[now.end] = true;        // 방문 처리
            }

            // 현재 정점에서 방문 가능한 정점 순회
            for (int i = 0; i < list[now.end].size(); i++) {
                Node next = list[now.end].get(i);
                if (!visited[next.end] && now.weight + next.weight < result[next.end]) {
                    result[next.end] = now.weight + next.weight;
                    queue.add(new Node(next.end, result[next.end]));
                }
            }

        }

        // 출력
        for (int i = 1; i <= V; i++) {
            if (result[i] == Integer.MAX_VALUE) {
                System.out.println("INF");
            } else {
                System.out.println(result[i]);
            }
        }





    }
}
