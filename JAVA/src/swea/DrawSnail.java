package JAVA.src.swea;

import java.util.Scanner;

public class DrawSnail {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();

        for(int i = 0; i < T; i++){
            int N = sc.nextInt();
            drawSnail(N, i);
        }
    }

    private static void drawSnail(int n, int t){
        int[][] snail = new int[n][n];
        
        int turn = n;
        int k = 1; // 달팽이가 그릴 숫자
        int right = -1;
        int bottom = 0;
        int dir = 1;

        for(int i = turn; i > 0; i--){
            
            for(int j = 0; j < turn; j++){
                right += dir;
                snail[bottom][right] = k;
                k++;
            }

            turn--;

            for(int j = 0; j < turn; j++){
                bottom += dir;
                snail[bottom][right] = k;
                k++;
            }

            dir = dir * (-1);

        }

        // 달팽이가 그린 숫자 출력하기
        System.out.println("#" + (t + 1));
        for(int i = 0; i < snail.length; i++){
            for(int j = 0; j < snail[i].length; j++){
                System.out.print(snail[i][j] + " ");
            }
            System.out.println();;
        }

        
    }
    
}
