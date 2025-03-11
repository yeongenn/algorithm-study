package JAVA.src.swea.Tree;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Node { // 트리 노드
    int index;
    String value;
    Node leftNode;
    Node rightNode;

    public Node(int index) {
        this.index = index;
        this.value = " "; // 초기값
        leftNode = null;
        rightNode = null;
    }
}

class Tree {
    Node root = null; // 해당 트리의 루트 노드

    public void add(int index, String value, int leftIndex, int rightIndex) {
        if (root == null) { // 트리 최초 생성
            root = new Node(index);
            root.value = value;

            // 자식 노드 있다면 노드 인덱스도 저장
            if (leftIndex != 0) {
                root.leftNode = new Node(leftIndex);
            }
            if (rightIndex != 0) {
                root.rightNode = new Node(rightIndex);
            }
        } else { // 트리 이미 있다면 찾아가기
            search(root, value, index, leftIndex, rightIndex);
        }
    }

    // 이미 있는 노드 찾아가서
    public void search(Node root, String value, int index, int leftIndex, int rightIndex) {
        if (root.index == index) {      // 노드 정보 저장하기
            root.value = value;
            if (leftIndex != 0) {
                root.leftNode = new Node(leftIndex);
            }
            if (rightIndex != 0) {
                root.rightNode = new Node(rightIndex);
            }
        } else {
            if (root.leftNode != null) {
                search(root.leftNode, value, index, leftIndex, rightIndex);
            }
            if (root.rightNode != null) {
                search(root.rightNode, value, index, leftIndex, rightIndex);
            }
        }
    }

    // 자식 노드 값 연산해서 그 결과 현재 노드에 저장하기
    // param root : 현재 단위에서 중위 노드
    public double inOrder(Node root) { 
        String curValue = root.value;
        double left = 0;
        double right = 0;

        if (root.leftNode != null && root.rightNode != null) {
            left = inOrder(root.leftNode);
            right = inOrder(root.rightNode);

            if (curValue.equals("+")) {
                root.value = String.valueOf(left + right);
            } else if (curValue.equals("-")) {
                root.value = String.valueOf(left - right);
            } else if (curValue.equals("*")) {
                root.value = String.valueOf(left * right);
            } else if (curValue.equals("/")) {
                root.value = String.valueOf(left / right);
            }

        }

        return Double.parseDouble(root.value);
    }
}

public class Operations {
    static int n; // 노드 수
    static Tree tree;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = null;

        for (int i = 0; i < 1; i++) { // 테케 10개
            n = Integer.parseInt(br.readLine());
            tree = new Tree();

            for (int j = 0; j < n; j++) {  
                st = new StringTokenizer(br.readLine());
                st.nextToken();
                String value = st.nextToken();
                int leftIndex = 0;
                int rightIndex = 0;

                if (st.countTokens() > 0) { // 자식 노드 있으면
                    leftIndex = Integer.parseInt(st.nextToken());
                    rightIndex = Integer.parseInt(st.nextToken());
                }

                tree.add(j + 1, value, leftIndex, rightIndex);   // 인덱스가 이렇게 중요합니다 ㅅㅂ
            }

            System.out.println("#" + (i + 1) + " " + (int) tree.inOrder(tree.root));
        }
    }
}
