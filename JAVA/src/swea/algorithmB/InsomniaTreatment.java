package JAVA.src.swea.algorithmB;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;

public class InsomniaTreatment {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        StringBuilder sb = new StringBuilder();

        for (int t = 1; t <= T; t++) {
            int N = Integer.parseInt(br.readLine());
            Set<Character> digitSet = new HashSet<>();
            int k = 0;

            while (digitSet.size() < 10) {
                k++;
                int multiple = N * k;
                for (char ch : String.valueOf(multiple).toCharArray()) {
                    digitSet.add(ch);
                    if (digitSet.size() == 10) break;
                }
            }

            sb.append("#").append(t).append(" ").append(N * k).append("\n");

        }

        System.out.println(sb.toString());
    }
}
