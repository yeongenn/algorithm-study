import java.util.Arrays;
import java.util.Scanner;

public class Solution2 {

    // SWEA 2063. 중간값 찾기
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        // 테스트 케이스 수
        int T = sc.nextInt();

        // 중간값 인덱스
        int medianIndex = (T/2) + 1;

        int[] arr = new int[T];

        for (int i = 0 ; i <= T - 1 ; i++){
            arr[i] = sc.nextInt();
        }

        // 정렬
        for (int i = 0 ; i < arr.length - 1 ; i++){
            for (int j = 0 ; j < arr.length - 1 - i ; j++){
                if (arr[j] > arr[j + 1]){
                    int temp = arr[j + 1];
                    arr[j + 1] = arr[j];
                    arr[j] = temp;
                }
            }
        }

        // 출력
        System.out.println(arr[medianIndex - 1]);

        sc.close();

    }

}
