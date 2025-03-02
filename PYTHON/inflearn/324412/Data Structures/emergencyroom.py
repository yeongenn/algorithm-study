# 나는 백강혁이다~!
# priority queue

N, M = map(int, input().split())
patients = list(map(int, input().split()))


order = 1   # 치료받을 순서
while patients:
    first = max(patients)   # 우선순위 갱신

    if patients[0] == first:
        if M == 0:
            print(order)
            break
        else:
            patients.pop(0)
            order += 1
    else:
        patients.append(patients.pop(0))
        
    M = M - 1 if M > 0 else len(patients) - 1   # 첫번째 문서 프린트하든 뒤로 보내든 M은 갱신되어야!
        
    