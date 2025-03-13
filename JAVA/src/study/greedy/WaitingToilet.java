package JAVA.src.study.greedy;

import java.util.Arrays;

public class WaitingToilet {

    /*
     * 그리디 문제
     * 
     * 2. 화장실 문제
     * 하나의 화장실, A ~ D 평균 사용 시간 {15, 30, 50, 10}
     * 이때 대기시간 누적합 최소 만들기
     * 
     */

    public static void main(String[] args) {
        int[] people = {15, 30, 50, 10};    // 대기 시간
        int n = people.length;

        Arrays.sort(people);    // 오름차순
        System.out.println(Arrays.toString(people));

        int totalTime = 0;
        int remainPeople = n - 1;

        for (int turn = 0; turn < n; turn++) {
            int time = people[turn];
            totalTime += time * remainPeople;
            remainPeople--;
        }

        System.out.println(totalTime);

    }

}
