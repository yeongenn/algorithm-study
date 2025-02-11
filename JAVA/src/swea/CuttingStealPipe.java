package JAVA.src.swea;

import java.util.Scanner;
import java.util.Stack;

public class CuttingStealPipe {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();

        for (int i = 1; i <= T; i++){
            int count = 0;
            Stack<Integer> pipe = new Stack<>();    // 막대기 관리
            String array = sc.next();
            array = array.replace("()", "L");
            for (int j = 0; j < array.length(); j++){
                if (String.valueOf(array.charAt(j)).equals("L")){
                    if (pipe.isEmpty()){    // 스택 비어있으면 통과
                        continue;
                    } else {    // 스택 사이즈만큼 조각 증가
                        count += pipe.size();
                    }
                } else if (String.valueOf(array.charAt(j)).equals("(")){    // 열린 괄호면 스택에 쌓기
                    pipe.push(1);
                } else {    // 닫힌 괄호면 pop하고 조각 증가
                    pipe.pop();
                    count += 1;
                }
            }
            System.out.println("#" + i + " " + count);
        }
    }
}
