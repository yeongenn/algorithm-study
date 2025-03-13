package JAVA.src.study.greedy;

import java.util.Scanner;

public class ChangeCoin {

    /*
     * 그리디 문제
     * 
     * 1. 동전 교환
     * 네 종류의 동전을 사용해 최소한의 동전 수로 거스름돈 N 내주기, N = 1730
     * 
     */
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int amount = sc.nextInt();

        int[] coinList = {500, 100, 50, 10};

        int possibleCnt = 0;
        int count = 0;
        for (int coin : coinList) {
            possibleCnt = (int) (amount / coin);
            
            count += possibleCnt;
            amount -= possibleCnt * coin;

        }

        System.out.println(count);

    }
    
}
