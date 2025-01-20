package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class Solution10773 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = null;
        Stack<Integer> myStack = new Stack<>();

        int sum = 0;

        st = new StringTokenizer(br.readLine());
        int T = Integer.parseInt(st.nextToken());
        for (int i = 1; i <= T; i++) {
            st = new StringTokenizer(br.readLine());
            int num = Integer.parseInt(st.nextToken());
            if (num != 0) {
                myStack.push(num);
            } else {
                myStack.pop();
            }
        }

        for (int i = 0; i < myStack.size(); i++) {
            sum += myStack.get(i);
        }

        System.out.println(sum);
        br.close();
    }
}