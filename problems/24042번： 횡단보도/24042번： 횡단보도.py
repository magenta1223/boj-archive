#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 24042                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/24042                         #+#        #+#      #+#     #
#     Solved: 2024-05-10 14:36:11 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

input = open(0).readline
 
from heapq import heappop, heappush
 
N,M = map(int,input().split())
G = {i : [] for i in range(1,N+1)}
# W = [[[] for _ in range(N+1)] for _ in range(N+1)]
 
for i in range(M):
    a,b = map(int,input().split())
    G[a].append((b,i))
    G[b].append((a,i))
    # W[a][b].append(i)
    # W[b][a].append(i)
 
INF = float("inf")
heap = [(0,1)]
costs = [INF] * (N+1)
costs[1] = 0
while heap:
    cur_cost, now = heappop(heap)
    if costs[now] < cur_cost:
        continue
    r = cur_cost % M
    for next, idx in G[now]:
        # 현재 가능한 edges 중 가장 빨리 이동 가능한 것 
        if idx < r:
            next_cost = cur_cost + (idx+M-r+1)
        else: 
            next_cost = cur_cost + (idx-r+1)
    
        if costs[next] > next_cost:
            costs[next] = next_cost 
            heappush(heap, (next_cost, next))
 
print(costs[-1]) 