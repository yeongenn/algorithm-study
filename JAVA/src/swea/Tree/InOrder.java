package JAVA.src.swea.Tree;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class InOrder {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = null;

        int T = 2;      // 확인용
        for (int i = 0; i < T; i++){
            int N = Integer.parseInt(br.readLine());
            String[] tree = new String[N + 1];

            for (int j = 0; j < N; j++){
                st = new StringTokenizer(br.readLine());
                int idx = Integer.parseInt(st.nextToken());
                String v = st.nextToken();
                
                if (st.hasMoreTokens()) {
                    int l = Integer.parseInt(st.nextToken());
                }

                if (st.hasMoreTokens()) {
                    int r = Integer.parseInt(st.nextToken());
                }

                tree[idx] = v;

            }

            // System.out.println(Arrays.deepToString(tree));
            System.out.println("#" + i + 1);
            readWords(tree, 1);
            System.out.println();
        }

    }

    static void readWords(String[] strArr, int n){        // 트리랑 루트 노드
        if (n < strArr.length) {
            readWords(strArr, n * 2);
            System.out.print(strArr[n]);
            readWords(strArr, n * 2 + 1);
        }
    }
}
