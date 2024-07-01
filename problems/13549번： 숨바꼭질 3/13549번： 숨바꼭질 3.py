#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 13549                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/13549                         #+#        #+#      #+#     #
#     Solved: 2024-01-29 17:24:39 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from collections import deque 
N,K=map(int, input().split())
 
queue = deque([[N, 0]])
visited = set()
costs = [float("inf") for _ in range(100_000+1)]
costs[N]=0
 
import heapq
heap = [(0, N)]
while heap:
    c, x = heapq.heappop(heap)
    if x == K:
        break 
    for _next in [x-1, x+1]:
        if 0<=_next<=100_000 and costs[_next] > c + 1:
            # queue.append([_next, c+1])
            heapq.heappush(heap, (c+1, _next))
            costs[_next] = c + 1
    _next = 2*x
    if 0<=_next<=100_000 and costs[_next] > c:
        costs[_next] = c
        heapq.heappush(heap, (c, _next))
print(costs[K])