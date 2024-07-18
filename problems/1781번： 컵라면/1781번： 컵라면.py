#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1781                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1781                          #+#        #+#      #+#     #
#     Solved: 2024-07-18 06:30:06 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


"""
3
1 25
2 50
2 100
"""

# 단순히 지금 deadline에 걸린 최대치를 사용하면 안됨. 
# 지금 t 
# deadline=t+1에서 최대인 task를 수행 시 -> deadline=t+2의 두 번째와 비교해야 함 
# 왜나면 이걸 하면 t+2의 2번째를 못하게 됨 



from heapq import heappop, heappush

input = open(0).readline 

N = int(input())
array = []
for _ in range(N):
    deadline, cupNoodle = map(int, input().split())
    array.append((deadline, cupNoodle))


# deadline 순으로 정렬 
array.sort()

heap = []

print(array)

for i in array:
    # deadline이 작은 순으로 
    # cupNoodle을 추가 
    heappush(heap, i[1])

    # 경과한 시간보다 deadline이 크면 추가 불가능. 가장 낮은거 하나 빼기.. 쉬발 돌았다리 
    if i[0] < len(heap):
        heappop(heap)
    
print(sum(heap))



"""
6
6 5
6 4
6 3
6 2
6 1
4 8

0 1 2 3 4 5 
1 2 3 8 4 5


3
1 25
2 50
2 100


"""

