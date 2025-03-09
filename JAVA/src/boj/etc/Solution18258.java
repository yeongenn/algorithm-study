package JAVA.src.boj.etc;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Solution18258 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = null;
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());

        // Queue<Integer> queue = new LinkedList<>();
        Deque<Integer> queue = new ArrayDeque<>();  // Deque로 큐 구현
        // int lastValue = 0;

        for (int i = 0; i < T; i++) {
            st = new StringTokenizer(br.readLine());

            switch(st.nextToken()){
                case "pop":
                    if (queue.isEmpty()){
                        sb.append(-1).append("\n");
                    } else {
                        sb.append(queue.poll()).append("\n");
                    }
                    break;
                case "size":
                    sb.append(queue.size()).append("\n");
                    break;
                case "empty":
                    if (queue.isEmpty()) {
                        sb.append(1).append("\n");
                    } else {
                        sb.append(0).append("\n");
                    }
                    break;
                case "front":
                    if (queue.isEmpty()) {
                        sb.append(-1).append("\n");
                    } else {
                        // sb.append(queue.peek()).append("\n");
                        sb.append(queue.getFirst()).append("\n");
                    }
                    break;
                case "back":
                    if (queue.isEmpty()) {
                        sb.append(-1).append("\n");
                    } else {
                        // sb.append(lastValue).append("\n");
                        sb.append(queue.getLast()).append("\n");    // 큐 마지막 요소소
                    }
                    break;
                case "push":
                    int x = Integer.parseInt(st.nextToken());
                    queue.add(x);
                    // lastValue = x;
                    break;
            }
        }

        System.out.println(sb.toString());
        br.close();
    }

}
