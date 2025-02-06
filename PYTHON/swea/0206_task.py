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

# 전기버스

# T = int(input())

# K : 최대 이동 정류장 수
# N : 종점 정류장
# M : 충전기 설치된 정류장 수
K, N, M = map(int, input().split())

stt_loc = list(map(int, input().split()))


    
    
    
        


    

    
    

    

    



      



    


    

    

