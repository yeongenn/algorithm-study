package JAVA.src.boj;

import java.util.Scanner;

public class Solution25314 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();

        int lCount = T / 4;
        for(int i = 0; i < lCount; i++){
            System.out.print("long ");
        }

        System.out.print("int");
    }
    
}
