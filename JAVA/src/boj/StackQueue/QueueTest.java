package JAVA.src.boj.StackQueue;

import java.util.LinkedList;
import java.util.Queue;

public class QueueTest {

    public static void main(String[] args) {
        // Queue : FIFO
        // 자바에서 Queue 구현할 때 LinkedList로 많이 구현한다
        Queue<Integer> queue = new LinkedList<>();

        // 요소 추가
        // add : 성공 시 True, 가용공간 없을 경우 IllegalStateException 반환
        // offer : 성공 시 True, 실패 시 False
        queue.add(1);
        queue.offer(2);
        queue.add(10);
        queue.add(11);

        // 요소 삭제
        // poll : 첫번째 값 제거한 후 해당 값 반환, 비어있다면 null 반환
        // remove : 첫번째 값 제거한 후 해당 값 반환, 비어있다면 NoSuchElementException
        // clear : 모든 요소 제거

        // 이때 clear는 Queue 인터페이스에 존재하지 X
        // clear 쓰려면?
        // LinkedList로 선언해서 사용

        System.out.println(queue.poll());
        System.out.println(queue.remove());
        System.out.println(queue);

        // 요소 검색
        // peek : 첫번째 값 반환, 비어있으면 null
        // element : 첫번째 값 반환, 비어있으면 NoSuchElementException

        System.out.println(queue.peek());
        System.out.println(queue.poll());
        System.out.println(queue.element());
        System.out.println(queue);

    }

}
