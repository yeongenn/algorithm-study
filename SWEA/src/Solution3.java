import java.util.Arrays;
import java.util.Scanner;

public class Solution3 {

    // SWEA 1959. 두 개의 숫자열
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);

        // 테스트 케이스 수
        int T = sc.nextInt();

        // A, B 배열 크기
        int A_size = sc.nextInt();
        int B_size = sc.nextInt();

        // 빈 배열 생성
        int[] arr_A = new int[A_size];
        int[] arr_B = new int[B_size];

        // A 배열
        for(int i = 0 ; i < arr_A.length; i++){
            arr_A[i] = sc.nextInt();
        }

        // System.out.println(Arrays.toString(arr_A));

        // B 배열
        for(int i = 0 ; i < arr_B.length; i++){
            arr_B[i] = sc.nextInt();
        }

        // 확인
        // System.out.println(Arrays.toString(arr_A));
        // System.out.println(Arrays.toString(arr_B));

        // 



    }
    
}
