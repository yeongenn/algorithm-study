package JAVA.src.boj.Deque;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;
import java.util.stream.IntStream;

public class Enumerate {

    public static void main(String[] args) {
        // Java로 enumerate 구현하기
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] papers = new int[N];
        for (int i = 0; i < N; i++){
            papers[i] = sc.nextInt();
        }

        // IntStream.range(0, papers.length).forEach(idx -> {
            //     int paper = papers[idx];
            //     System.out.println((idx + 1) + " : " + paper);
            // });
            
        List<int[]> list = new ArrayList<>();
        IntStream.range(0, papers.length).forEach(idx -> {
            int paper = papers[idx];
            int[] elem = {idx + 1, paper};
            list.add(idx, elem);
        });

        // System.out.println(Arrays.toString(papers));

        for (int[] is : list) {
            // System.out.println(is[0] + " : " + is[1]);
            System.out.println(Arrays.toString(is));
        }

        // Java로 rotate 사용하기
        Collections.rotate(list, 1);    // 양수면 오른쪽
        System.out.println(Arrays.deepToString(list.toArray()));
        Collections.rotate(list, -1);   // 음수면 왼쪽
        System.out.println(Arrays.deepToString(list.toArray()));
    }
    
}
