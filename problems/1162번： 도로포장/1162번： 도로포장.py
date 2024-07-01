#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1162                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1162                          #+#        #+#      #+#     #
#     Solved: 2024-05-27 10:30:38 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

input = open(0).readline 
 
from heapq import heappop, heappush 
INF = float("inf")
 
N,M,K = map(int,input().split())
G = {i : [] for i in range(1,N+1)}
for _ in range(M):
    a,b,c = map(int,input().split())
    G[a].append((b,c))
    G[b].append((a,c))
 
# 다익스트라를 k번하면 됨 
COSTS = [[INF] * (N+1) for _ in range(K+1)]
 
def daijkstra(k):
    heap = [(0,1)]
    COSTS[k][1] = 0 
    while heap:
        cur_cost, now = heappop(heap)
        if COSTS[k][now] < cur_cost:
            continue 
        for next, _c in G[now]:
            next_cost = cur_cost + _c 
            # 도로 하나 생략 
            if COSTS[k][next] > COSTS[k-1][now]:
                COSTS[k][next] = COSTS[k-1][now]
                heappush(heap, (COSTS[k-1][now], next))
            if COSTS[k][next] > next_cost:
                COSTS[k][next] = next_cost
                heappush(heap, (next_cost, next))
 
heap = [(0,1)]
COSTS[0][1] = 0
while heap:
    cur_cost, now = heappop(heap)
    if COSTS[0][now] < cur_cost:
        continue 
    for next, _c in G[now]:
        next_cost = cur_cost + _c 
        # 도로 하나 생략 
        if COSTS[0] [next] > next_cost:
            COSTS[0][next] = next_cost
            heappush(heap, (next_cost, next))
for k in range(1,K+1):
    daijkstra(k)
print(COSTS[K][N])