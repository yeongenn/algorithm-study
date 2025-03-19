package JAVA.src.boj.UnionFind;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class SetExpression {

    static int[] parent;


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = null;

        st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        parent = new int[N + 1];
        makeSet(parent);
        
        for (int i = 0; i < M; i++){
            st = new StringTokenizer(br.readLine());
            int Q = Integer.parseInt(st.nextToken());
            int A = Integer.parseInt(st.nextToken());
            int B = Integer.parseInt(st.nextToken());

            if (Q == 0) {       // A, B 합치기
                union(A, B);
            } else {            // A, B가 같은 집합에 포함되어 있는지
                if (findSet(A) != findSet(B)) {
                    System.out.println("NO");
                } else {
                    System.out.println("YES");
                }
            }
        }
    }

    static void makeSet(int[] parent) { // 초기화
        int n = parent.length - 1;
        for (int i = 1; i <= n; i++) {
            parent[i] = i;
        }
    }

    static int findSet(int x) {
        if (parent[x] != x) {
            parent[x] = findSet(parent[x]);
        }
        return parent[x];
    }

    static void union(int a, int b) {
        a = findSet(a);
        b = findSet(b);

        if (a < b) {
            parent[b] = a;
        } else {
            parent[a] = b;
        }

        // 오답 코드        <- 뭔 차이?
        // if (a < b) {
        //     parent[b] = a;
        // } else if (b > a) {
        //     parent[a] = b;
        // } else {        // 이미 같은 집합이면~
        //     return;
        // }
    }
    
}
