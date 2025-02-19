package JAVA.src.boj.Deque;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class Solution28279 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = null;
        StringBuilder sb = new StringBuilder();
        int T = Integer.parseInt(br.readLine());

        Deque<Integer> deque = new ArrayDeque<>();
        for (int i = 0; i < T; i++) {
            st = new StringTokenizer(br.readLine());
            int x = 0;

            switch (Integer.parseInt(st.nextToken())) {
                case 1:
                    x = Integer.parseInt(st.nextToken());
                    deque.addFirst(x);
                    break;
                case 2:
                    x = Integer.parseInt(st.nextToken());
                    deque.addLast(x);
                    break;
                case 3:
                    if (!deque.isEmpty()) {
                        sb.append(deque.removeFirst() + "\n");
                    } else {
                        sb.append(-1 + "\n");
                    }
                    break;
                case 4:
                    if (!deque.isEmpty()) {
                        sb.append(deque.removeLast() + "\n");
                    } else {
                        sb.append(-1 + "\n");
                    }
                    break;
                case 5:
                    sb.append(deque.size() + "\n");
                    break;
                case 6:
                    if (!deque.isEmpty()) {
                        sb.append(0 + "\n");
                    } else {
                        sb.append(1 + "\n");
                    }
                    break;
                case 7:
                    if (!deque.isEmpty()) {
                        sb.append(deque.peekFirst() + "\n");
                    } else {
                        sb.append(-1 + "\n");
                    }
                    break;
                case 8:
                    if (!deque.isEmpty()) {
                        sb.append(deque.peekLast() + "\n");
                    } else {
                        sb.append(-1 + "\n");
                    }
                    break;
            }

        }
        System.out.println(sb.toString());
        br.close();
    }

}
