package JAVA.src.swea;

import java.util.LinkedList;
import java.util.Stack;

class Graph {
    class Node {
        int data; // 정수 데이터
        LinkedList<Node> adjacent; // 인접한 노드들과의 관계는 LinkedList로 표현
        boolean marked; // 방문했는지 마킹하는 플래그

        Node(int data) {
            this.data = data;
            this.marked = false;
            adjacent = new LinkedList<Node>();
        }
    }

    Node[] nodes; // 노드들을 저장할 배열

    Graph(int size) { // 노드 갯수는 고정
        nodes = new Node[size];
        for (int i = 0; i < size; i++) {
            nodes[i] = new Node(i); // 편의 위해서 동일하게
        }
    }

    void addEdge(int i1, int i2) { // 두 노드의 관계를 저장하는 함수
        // 데이터가 인덱스와 같으니까 받은 숫자를 인덱스로 사용 가능
        Node n1 = nodes[i1];
        Node n2 = nodes[i2];

        // 두 개의 노드에 인접한 노드를 저장하는 LinkedList에 상대방이 있는지 확인하고 서로 추가해주기
        if (!n1.adjacent.contains(n2)) {
            n1.adjacent.add(n2);
        }
        if (!n2.adjacent.contains(n1)) {
            n2.adjacent.add(n1);
        }
    }

    void dfs() { // dfs 함수를 그냥 호출하면 0번부터 시작하도록
        dfs(0);
    }

    void dfs(int index) { // 인덱스 받아서 dfs 순회 결과 출력하는 함수
        Node root = nodes[index]; // 해당 인덱스로 노드 가져오기
        Stack<Node> stack = new Stack<>(); // 스택 하나 생성
        stack.push(root); // 현재 노드를 스택에 추가
        root.marked = true; // 스택에 들어갔다고 표시해주기
        while (!stack.isEmpty()) { // 스택에 데이터가 없을 때까지 반복
            Node r = stack.pop(); // 스택에서 데이터 하나 가져오기
            for (Node n : r.adjacent) { // 가져온 노드의 자식들을 스택에 추가
                if (!n.marked) { // 이때 스택에 추가되지 않은 노드들만 추가
                    n.marked = true;
                    stack.push(n);
                }
            }
            visit(r); // 출력
        }
    }

    void visit(Node n) { // 방문할 때 출력해주는 함수
        System.out.print(n.data + " ");
    }

}

public class GraphSearch1 {

    public static void main(String[] args) {
        Graph g = new Graph(9);
        g.addEdge(0, 1);
        g.addEdge(1, 2);
        g.addEdge(1, 3);
        g.addEdge(2, 4);
        g.addEdge(2, 3);
        g.addEdge(3, 4);
        g.addEdge(3, 5);
        g.addEdge(5, 6);
        g.addEdge(5, 7);
        g.addEdge(6, 8);

        // 그래프 확인용
        System.out.println();
        for(int i = 0; i < 9; i++){
            System.out.print(i + "번 노드 : ");
            for(int j = 0; j < g.nodes[i].adjacent.size(); j++){
                System.out.print(g.nodes[i].adjacent.get(j).data + " ");
            }
            System.out.println();
        }

        System.out.println();
        g.dfs(); // 아무것도 안 넘기면 0부터 시작
        // g.dfs(3);
    }
}