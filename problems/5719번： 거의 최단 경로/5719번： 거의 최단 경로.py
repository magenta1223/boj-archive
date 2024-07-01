#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 5719                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/5719                          #+#        #+#      #+#     #
#     Solved: 2024-06-03 15:38:21 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from heapq import heappop, heappush
from collections import deque
 
input = open(0).readline
INF = float("inf")
 
def daijkstra():
    heap = [(0,S)]
    costs = [INF] * N
    costs[S] = 0
    while heap:
        cur_cost, now = heappop(heap)
        for next,c in G[now]:
            next_cost = cur_cost+c
            if E[now][next] and costs[next] > next_cost:
                costs[next] = next_cost
                heappush(heap, (next_cost, next)) 
    return costs
 
def backtrack(costs):
    q = deque([D])
    while q:
        now = q.popleft()
        for prev, c in revG[now]: 
            if costs[prev]+c == costs[now] and E[prev][now]:
                # 비활성화 
                q.append(prev)
                E[prev][now] = False 
ans = []
 
while True:
    N,M = map(int,input().split())
    if N==M==0:
        break 
    S,D = map(int,input().split())
 
    G = {i : [] for i in range(N)}
    revG = {i : [] for i in range(N)}
 
    E = [[False] * N for _ in range(N)]
    for i in range(M):
        a,b,c = map(int,input().split())
        G[a].append((b,c))
        revG[b].append((a,c))
        E[a][b] = True
    
    # daijkstra 
    costs = daijkstra()
    # backtrack 
    backtrack(costs)
    costs = daijkstra()
    ans.append(costs[D] if costs[D] != INF else -1)
 
print(*ans, sep = '\n')