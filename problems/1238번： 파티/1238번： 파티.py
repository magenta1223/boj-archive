#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1238                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1238                          #+#        #+#      #+#     #
#     Solved: 2024-03-29 20:30:18 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from heapq import heappop, heappush
input = open(0).readline
 
N,M,X = map(int,input().split())
INF = float("inf")
 
G = {i : [] for i in range(N+1)}
for _ in range(M):
    a,b,t = map(int,input().split())
    G[a].append((b,t)) 
 
def daijkstra(n):
    heap = [(0, n)]
    dist = [INF for i in range( N+1)]
    dist[n] = 0
    
    while heap:
        cur_cost, cur_node = heappop(heap)
        for n_node, n_cost in G[cur_node]:
            n_cost = cur_cost + n_cost
            if dist[n_node] > n_cost:
                heappush(heap, (n_cost, n_node))
                dist[n_node] = n_cost
    dist[0] = 0
    return dist  
dists = [0] + [daijkstra(node) for node in range(1,N+1)]
 
print(max([dists[i][X] + dists[X][i]  for i in range(1,N+1)]))