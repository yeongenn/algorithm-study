package JAVA.src.swea;

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;
import java.util.Stack;

public class MatchingBrace {
    public static void main(String[] args) {
        // Stack 하나만 사용하기
        Scanner sc = new Scanner(System.in);
        Map<String, String> braceMap = new HashMap<>();
        braceMap.put(")", "(");
        braceMap.put("]", "[");
        braceMap.put("}", "{");
        braceMap.put(">", "<");

        for (int i = 1; i <= 10; i++){
            int N = sc.nextInt();
            String braces = sc.next();
            Stack<String> stack = new Stack<>();

            for(int j = 0; j < N; j++){ // braces 순회
                String brace = String.valueOf(braces.charAt(j));
                if (brace.equals("(") || brace.equals("[") || brace.equals("{") || brace.equals("<")) { // 열.괄
                    stack.push(brace);
                } else {    // 닫.괄
                    if (!stack.isEmpty() && stack.peek().equals(braceMap.get(brace))){
                        stack.pop();
                    } else { break; }
                }

            }
            int result = 0;
            if (!stack.isEmpty()){
                result = 0;
            } else { result = 1; }


            // 유효하면 1, 유효하지 않으면 0
            System.out.println("#" + i + " " + result);
        }
    }
    
}
