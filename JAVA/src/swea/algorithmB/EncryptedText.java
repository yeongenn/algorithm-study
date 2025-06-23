package JAVA.src.swea.algorithmB;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class EncryptedText {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer stk;
        LinkedList<String> encryptedText;
        for (int t = 1; t <= 10; t++) {
            encryptedText = new LinkedList<>();
            br.readLine();      //  원본 암호문 길이, 없어도 될..?
            stk = new StringTokenizer(br.readLine(), " ");      // " " 구분자로 끊기
            while (stk.hasMoreTokens()) {       // 각 암호문 리스트에 넣기
                encryptedText.add(stk.nextToken());
            }

            br.readLine();      // 명령어 갯수, 마찬가지로 없어도 될..?
            stk = new StringTokenizer(br.readLine(), " ");
            int x, y;
            while (stk.hasMoreTokens()) {
                // if-else if 구문으로 하니 메모리 초과 뜬다
                switch (stk.nextToken()) {
                    case "I":
                        // 앞에서부터 x번째 암호문 바로 다음에 y개 암호문 삽입
                        x = Integer.parseInt(stk.nextToken());
                        y = Integer.parseInt(stk.nextToken());
                        for (int i = 0; i < y; i++) {
                            encryptedText.add(x, stk.nextToken());
                            x++;
                        }
                        break;
                    case "D":
                        // 앞에서부터 x번째 암호문 바로 다음부터 y개 암호문 삭제
                        x = Integer.parseInt(stk.nextToken());
                        y = Integer.parseInt(stk.nextToken());
                        for (int i = 0; i < y; i++) {
                            encryptedText.remove(x);
                        }
                        break;
                    case "A":
                        // 암호문 맨 뒤에 y개 암호문 추가
                        y = Integer.parseInt(stk.nextToken());
                        for (int i = 0; i < y; i++) {
                            encryptedText.add(stk.nextToken());
                        }
                        break;
                }
            }
            // 암호문 앞 10개 출력
            System.out.println("#" + t + " ");
            for (int i = 0; i < 10; i++) {
                System.out.println(encryptedText.get(i) + " ");
            }
            System.out.println();
        }
    }
}
