package JAVA.src.boj;

import java.util.Arrays;

public class BubbleSort {
    
    public static void main(String[] args) {
        
        // 1 ~ 100 사이 자연수 랜덤 배열 생성
        int[] arr = new int[10];
        for(int i = 0 ; i < arr.length ; i++){
            arr[i] = (int) (Math.random() * 100) + 1;
        }

        System.out.println("Before : " + Arrays.toString(arr));

        // 버블 정렬
        for(int i = arr.length; i > 0; i--){
            for(int j = 0; j < i - 1; j++){
                if (arr[j] > arr[j + 1]) {
                    int temp = arr[j + 1];
                    arr[j + 1] = arr[j];
                    arr[j] = temp;
                }
            }
        }
        
        System.out.println("After : " + Arrays.toString(arr));        
    }
}
