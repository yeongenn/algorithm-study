# 250206 알고리즘 과제
# List

# Flatten - 평탄화

# def dump(box_list, max_idx, min_idx):
#     box_list[max_idx] -= 1
#     box_list[min_idx] += 1

# for t in range(10):

#     max_dump_count = int(input())
#     boxes = list(map(int, list(input().split())))

#     dump_count = 0
#     while dump_count < max_dump_count:

#         max_box_height = max(boxes)
#         min_box_height = min(boxes)

#         # max_box_index = 0
#         # min_box_index = 0

#         # for i in range(100):
#         #     if boxes[i] == max_box_height:
#         #         max_box_index = i
#         #         continue
#         #     if boxes[i] == min_box_height:
#         #         min_box_index = i
#         #         continue
        
#         # index 구하는 함수 있음ㅠㅠ
#         max_box_index = boxes.index(max_box_height)
#         min_box_index = boxes.index(min_box_height)

#         if (boxes[max_box_index] - boxes[min_box_index]) == 0 or (boxes[max_box_index] - boxes[min_box_index]) == 1:
#             break
#         else:
#             dump(boxes, max_box_index, min_box_index)
#             dump_count += 1

#     print(f'#{t + 1} {max(boxes) - min(boxes)}')


#########################################################################################################

# # 전기 버스

# T = int(input())
# for t in range(T):
#     # K : 이동 가능한 최대 정류장 수
#     # N : 종점
#     # M : 설치된 충전기 수
#     K, N, M = map(int, input().split())

#     stt_loc = list(map(int, input().split()))
#     stt_loc.append(0)

#     move = K
#     fill = 0
#     fill_loc = []  # 확인용

#     for i in range(M):
#         if i == 0:
#             move -= stt_loc[i]
#         else:
#             move -= stt_loc[i] - stt_loc[i - 1]

#         if i == (M - 1):
#             if stt_loc[i] + move >= N:
#                 break
#             else:
#                 fill += 1
#                 # fill_loc.append(stt_loc[i])
#                 move = K

#         if stt_loc[i] + move >= stt_loc[i + 1]:
#             continue
#         else:
#             fill += 1
#             # fill_loc.append(stt_loc[i])
#             move = K
#             if stt_loc[i] + move < stt_loc[i + 1]:
#                 fill = 0
#                 break


#     # print(fill)
#     # print(fill_loc)

#     print(f'#{t + 1} {fill}')

#########################################################################################################

# 간단한 소인수 분해

T = int(input())
dv = [2, 3, 5, 7, 11]

for t in range(T):
    dv_count = [0] * 12
    N = int(input())
    
    for num in dv:
        while N % num == 0:
            dv_count[num] += 1
            N /= num

    result = []
    for num in dv:
        result.append(dv_count[num])

    # print(result)

    print(f'#{t + 1}', *result)

#########################################################################################################
    
    
        


    

    
    

    

    



      



    


    

    

