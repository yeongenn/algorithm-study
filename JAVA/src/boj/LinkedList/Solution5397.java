package JAVA.src.boj.LinkedList;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.ListIterator;

public class Solution5397 {
    static LinkedList<Character> llist;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        for (int i = 0; i < T; i++) {
            llist = new LinkedList<>();
            ListIterator<Character> lIter = llist.listIterator();   // 연결리스트는 자바로?!
            String str = br.readLine();
            for (int j = 0; j < str.length(); j++) {
                char ch = str.charAt(j);
                switch (ch) {
                    case '<':
                        if (lIter.hasPrevious()) {
                            lIter.previous();
                        }
                        break;
                    case '>':
                        if (lIter.hasNext()) {
                            lIter.next();
                        }
                        break;
                    case '-':
                        if (lIter.hasPrevious()) {
                            lIter.previous();
                            lIter.remove(); // 마지막 요소 삭제
                        }
                        break;
                    default:    // 문자일 때
                        lIter.add(ch);  // 현재 위치 다음에 insert
                }
                
            }

            StringBuilder sb = new StringBuilder();
                for (char c : llist){
                    sb.append(c);
                }

                System.out.println(sb.toString());
        }
    }
}
