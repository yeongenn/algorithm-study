import sys
# sys.stdin = open("C:\\Users\\SSAFY\\Desktop\\YH\\algo-python\\PYTHON\\boj\\input.txt", "r")
sys.stdin = open("C:\\SSAFY\\algo-python\\PYTHON\\boj\\input.txt", "r")

def find_parent(x):
    if parents[x] != x:
        parents[x] = find_parent(parents[x])
    return parents[x]

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
            parents[B] = B

        pa = find_parent(A)
        pb = find_parent(B)
        if pa != pb:
            parents[pb] = pa
            network[pa] += network[pb]
            
        print(network[parents[A]])
        
######################################### review #########################################

# 내가 놓쳤던 부분 -> union 하는 부분

    # if find_parent(A) != find_parent(B):
    #     parents[B] = parents[A]
    #     network[parents[A]] += network[B]

# if문 안에서 네트워크 대장을 비교했어야 하는데
# 바로 위 네트워크를 비교했다