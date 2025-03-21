import sys
sys.stdin = open("C:\\Users\\SSAFY\\Desktop\\YH\\algo-python\\PYTHON\\boj\\input.txt", "r")

T = int(input())
for t in range(T):
    F = int(input())        # F < 100000
    network = {}
    parents = {}
    for f in range(F):
        A, B = input().split()
        if A not in network:
            network[A] = 1
            parents[A] = A      # 네트워크에 없었으면 자기자신이 부모
            
        if B not in network:
            network[B] = 1
            parents[B] = parents[A]     # A의 부모와 연결
            
            