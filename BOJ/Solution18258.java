package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Solution18258 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = null;
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());

        Queue<Integer> queue = new LinkedList<>();
        int lastValue = 0;

        for (int i = 0; i < T; i++) {
            String str = br.readLine();

            switch(str){
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
                        sb.append(queue.peek()).append("\n");
                    }
                    break;
                case "back":
                    if (queue.isEmpty()) {
                        sb.append(-1).append("\n");
                    } else {
                        sb.append(lastValue).append("\n");
                    }
                    break;
                default:
                    st = new StringTokenizer(str);
                    st.nextToken();
                    int x = Integer.parseInt(st.nextToken());
                    queue.add(x);
                    lastValue = x;
                    break;
            }
        }

        System.out.println(sb.toString());
        br.close();
    }

}
