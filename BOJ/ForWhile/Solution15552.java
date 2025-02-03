package BOJ.ForWhile;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Solution15552 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = null;
        // StringBuilder sb = new StringBuilder();
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));


        int T = Integer.parseInt(br.readLine());
        for(int i = 0; i < T; i++){
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            bw.write(a + b + "\n");
        }

        bw.flush();
    }

    /*
     * StringBuilder, BufferedReader 차이
     * 
     * StringBuilder
     * 문자열 조작이 빠르다
     * 추가 및 수정이 용이
     * 문자열 출력 기능이 없다
     * 
     * BufferedReader
     * 버퍼 제공해 문자열 출력 시 I/O 작업 횟수 줄여준다
     * 한 번에 많은 양의 데이터 출력할 때 용이
     * 문자열 조작 기능이 없다
     */
    
}
