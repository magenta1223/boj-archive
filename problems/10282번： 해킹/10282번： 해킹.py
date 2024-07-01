#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 10282                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/10282                         #+#        #+#      #+#     #
#     Solved: 2024-04-02 13:36:41 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from heapq import heappop, heappush
input = open(0).readline 
INF = float("inf")
 
 
def daijkstra(c):
    heap = [(0,c)]
 
    while heap:
        cur_cost, cur_node = heappop(heap)
 
        for next_node, _c in G[cur_node]:
            next_cost = cur_cost + _c
            if visited[next_node] > next_cost:
                visited[next_node] = next_cost
                heappush(heap, (next_cost, next_node))
 
 
for _ in range(int(input())):
    N,D,C = map(int,input().split())
    G = {i : [] for i in range(N+1)}
    visited = [INF] * (N+1) 
    ans = 0 
    for _ in range(D):
        a,b,s = map(int,input().split())
        G[b].append((a,s))
 
    # C부터 감염시작! -> dfs로 감염 
    visited[C] = 0
    daijkstra(C)
    hacked, ans = 0,0 
    for i in range(1,N+1):
        if visited[i] != INF:
            hacked += 1
            ans = max(ans, visited[i])
    print(hacked, ans)
    
 