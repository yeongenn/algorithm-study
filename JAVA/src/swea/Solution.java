package JAVA.src.swea;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Solution {

    // SWEA 1963. 1대1 가위바위보
    public static void main(String[] args) {

        // 2058.
        // int sum = 0;
        
        // Scanner sc = new Scanner(System.in);
        // int num = sc.nextInt();

        // while (num > 0) {
        //     int a = num % 10;
        //     sum += a;
        //     num /= 10;
        // }

        // System.out.println(sum);

        // 
        Scanner sc = new Scanner(System.in);
        String str = sc.nextLine();
        StringTokenizer st = new StringTokenizer(str, " ");

        int A = Integer.parseInt(st.nextToken());
        int B = Integer.parseInt(st.nextToken());

        if (A > B) {
            System.out.println("A");   
        } else {
            System.out.println("B");
        }

    }
}
