#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 7662                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/7662                          #+#        #+#      #+#     #
#     Solved: 2024-03-29 18:21:25 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from heapq import heappop, heappush
input = open(0).readline
 
def sync_pop(heap, deleted, pop = True):
    # heap이 있고, 해당 연산이 삭제되었다면 -> 제거 
    while heap and deleted[heap[0][1]]:
        heappop(heap)
    if pop and heap:
        # 제거 가능하다면 : 제거
        deleted[heap[0][1]] = True # 다른 heap에서 동기화할 때 제거하기 위해 
        heappop(heap)
 
 
for _ in range(int(input())):
    K = int(input())
    min_h, max_h, deleted =[], [], [True] * K # n의 범위가 너무큼. k로 
    for i in range(K):
        oper, n = input().split()
        n = int(n)
        if oper == "D":
            sync_pop(max_h if n == 1 else min_h, deleted)
        else:
            heappush(min_h, (n,i))
            heappush(max_h, (-n,i))
            deleted[i] = False
    
    # 동기화 
    sync_pop(max_h, deleted, False)
    sync_pop(min_h, deleted, False)
 
    if min_h:
        print(-heappop(max_h)[0], heappop(min_h)[0])
    else:
        print("EMPTY")