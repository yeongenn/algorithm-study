# 전기 버스

T = int(input())
for t in range(T):
    # K : 이동 가능한 최대 정류장 수
    # N : 종점
    # M : 설치된 충전기 수
    K, N, M = map(int, input().split())

    stt_loc = list(map(int, input().split()))
    stt_loc.append(0)

    move = K
    fill = 0
    fill_loc = []  # 확인용

    for i in range(M):
        if i == 0:
            move -= stt_loc[i]
        else:
            move -= stt_loc[i] - stt_loc[i - 1]

        if i == (M - 1):
            if stt_loc[i] + move >= N:
                break
            else:
                fill += 1
                # fill_loc.append(stt_loc[i])
                move = K

        if stt_loc[i] + move >= stt_loc[i + 1]:
            continue
        else:
            fill += 1
            # fill_loc.append(stt_loc[i])
            move = K
            if stt_loc[i] + move < stt_loc[i + 1]:
                fill = 0
                break


    # print(fill)
    # print(fill_loc)

    print(f'#{t + 1} {fill}')