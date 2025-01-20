package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class Solution28278 {

    // Stack

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = null;
        StringBuilder sb = new StringBuilder();

        Stack<Integer> myStack = new Stack<>();

        int T = Integer.parseInt(br.readLine());
        for (int i = 1; i <= T; i++) {
            // int order = br.read();
            st = new StringTokenizer(br.readLine());
            int order = Integer.parseInt(st.nextToken());
            switch (order) {
                case 1:
                    myStack.push(Integer.parseInt(st.nextToken()));
                    break;
                case 2:
                    if (!myStack.isEmpty()) {
                        sb.append(myStack.pop()).append("\n");
                    } else {
                        sb.append(-1).append("\n");
                    }
                    break;
                case 3:
                    sb.append(myStack.size()).append("\n");
                    break;
                case 4:
                    if (myStack.isEmpty()) {
                        sb.append(1).append("\n");
                    } else {
                        sb.append(0).append("\n");
                    }
                    break;
                case 5:
                    if (!myStack.isEmpty()) {
                        sb.append(myStack.peek()).append("\n");
                    } else {
                        sb.append(-1).append("\n");
                    }
                    break;
            }
        }
        System.out.println(sb.toString());
        br.close();
    }

}
