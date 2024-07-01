#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1916                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1916                          #+#        #+#      #+#     #
#     Solved: 2024-04-02 15:39:50 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from heapq import heappop, heappush
INF = float("inf")
input = open(0).readline 
N, M = int(input()), int(input())
G = {i : [] for i in range(1,N+1)}
for _ in range(M):
    a, b, c = map(int,input().split())
    G[a].append((b,c))
S,E = map(int,input().split())
heap = [(0, S)]
visited = [INF] * (N+1)
while heap:
    cur_cost, cur_node = heappop(heap)
    
    if cur_cost > visited[cur_node]:
        continue
 
    for next_node, _c in G[cur_node]:
        next_cost = cur_cost + _c 
        if visited[next_node] > next_cost:
            visited[next_node] = next_cost 
            heappush(heap, (next_cost, next_node))
 
print(visited[E])