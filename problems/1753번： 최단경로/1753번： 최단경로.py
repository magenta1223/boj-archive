#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1753                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1753                          #+#        #+#      #+#     #
#     Solved: 2024-01-29 15:16:27 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import heapq
input = open(0).readline
V, E = map(int, input().split())
K = int(input().strip())
G = {i: [] for i in range(1, V + 1)}
 
for _ in range(E):
    u, v, w = map(int, input().split())
    G[u].append((v, w))
 
costs = [float("inf") for _ in range(V+1)]
costs[K] = 0
heap = [(0, K)]
while heap:
    cur_cost, cur_node = heapq.heappop(heap)
    if cur_cost > costs[cur_node]: # 탐색 필요 x
        continue
    for v, w in G[cur_node]:
        if costs[v] > cur_cost + w:
            costs[v] = cur_cost + w
            heapq.heappush(heap, (costs[v], v))
    
for c in costs[1:]:
    print(str(c).upper())