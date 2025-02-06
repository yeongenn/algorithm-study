package JAVA.src.boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Solution10773 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // StringTokenizer 필요 X
        int T = Integer.parseInt(br.readLine());

        Stack<Integer> myStack = new Stack<>();

        int sum = 0;

        for (int i = 1; i <= T; i++) {
            int num = Integer.parseInt(br.readLine());
            if (num != 0) {
                myStack.push(num);
            } else {
                myStack.pop();
            }
        }

        // enhanced for
        // for(int i : myStack){
        // sum += i;
        // }

        // for
        // for (int i = 0; i < myStack.size(); i++) {
        // sum += myStack.get(i);
        // }

        // while
        while (!myStack.isEmpty()) {
            sum += myStack.pop();
        }

        System.out.println(sum);
        br.close();
    }
}