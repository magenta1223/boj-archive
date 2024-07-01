#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2176                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2176                          #+#        #+#      #+#     #
#     Solved: 2024-04-30 12:25:44 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from heapq import heappush, heappop 
 
def daijkstra(start):
    heap = [(0, start)]
    costs = [INF] * N
    while heap:
        cur_cost, cur_node = heappop(heap)
        if cur_cost > costs[cur_node]:
            continue 
        for next_node, c in G[cur_node]:
            next_cost = c+cur_cost 
            if costs[next_node] > next_cost:
                costs[next_node] = next_cost 
                heappush(heap, (next_cost, next_node))
    return costs[T]
 
def dfs(idx):
    if idx == T:
        return 1 
    if dp[idx] != -1:
        return dp[idx]
    dp[idx] = 0 
    for next_idx, _ in G[idx]:
        if COSTS[idx] <= COSTS[next_idx]:
            continue 
        dp[idx] += dfs(next_idx)
    return dp[idx]
 
input = open(0).readline 
INF = float("inf")
S,T = 0, 1
N,M = map(int,input().split())
G = {i : [] for i in range(N)}
 
for _ in range(M):
    a,b,c = map(int,input().split())
    a, b = a-1, b-1
    G[a].append((b,c))
    G[b].append((a,c))
 
COSTS = [INF] * N
for i in range(N):
    COSTS[i] = daijkstra(i)
COSTS[T] = 0
dp = [-1] * N
print(dfs(0))