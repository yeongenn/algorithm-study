package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Solution10951{

    // EOF : End of File
    public static void main(String[] args) throws IOException {
        // Scanner sc = new Scanner(System.in);
        // Scanner
        // hasNext(), hasNextInt(), hasNextLine()
        // while(sc.hasNext()){

        // }

        // BufferedReader
        // br.readline() == null
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st = null;
        String str = "";


        // 콘솔에서 입력 종료하려면 Ctrl + Z 후 엔터
        while((str = br.readLine()) != null){
            st = new StringTokenizer(str);
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            sb.append(a + b).append("\n");
        }

        System.out.println(sb.toString());
    }
}