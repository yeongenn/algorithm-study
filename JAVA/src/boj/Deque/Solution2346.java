package JAVA.src.boj.Deque;

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Deque;
import java.util.List;
import java.util.Scanner;
import java.util.stream.IntStream;

public class Solution2346 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int [] papers = new int[N];
        for (int i = 0; i < N; i++){
            papers[i] = sc.nextInt();
        }

        Deque<int[]> deque = new ArrayDeque<>();
        IntStream.range(0, papers.length).forEach(idx -> {
            int paper = papers[idx];
            int[] elem = {idx + 1, paper};
            deque.add(elem);
        });

        // Collections.rotate() 인자로 넘기기 위한 casting
        List<int[]> list = new ArrayList<>(deque);
        int[] result = new int[N];
        for (int j = 0; j < N - 1; j++){
//            int[] now = list.removeFirst();       // removeFirst: jdk 21 이후만 지원
            int[] now = list.remove(0);
            // int[] now = list.remove(0); // BOJ java11은 removeFirst() 지원 X
            int step = now[1];
            result[j] = now[0];
            
            int turn = 0;
            if (step > 0) {
                turn = -((step - 1) % list.size());
                // Collections.rotate(Arrays.asList(deque.toArray()), turn);    // rotate 작동 X
                Collections.rotate(list, turn);
            } else {
                turn = Math.abs(step) % list.size();
                // Collections.rotate(Arrays.asList(deque.toArray()), turn);
                Collections.rotate(list, turn);
            }

        }

        // 마지막 남은 풍선 터뜨리기
//        result[N - 1] = list.removeFirst()[0];        // removeFirst: jdk 21 이후만 지원
        result[N - 1] = list.remove(0)[0];
        // result[N - 1] = list.remove(0)[0];

        for (int i : result) {
            System.out.print(i + " ");
        }
    }
    
}
