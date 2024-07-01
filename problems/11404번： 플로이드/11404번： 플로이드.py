#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 11404                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/11404                         #+#        #+#      #+#     #
#     Solved: 2024-01-30 17:51:38 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from heapq import heappop, heappush
N=int(input().strip())
M=int(input().strip())
G = { i:[]  for i in range(N+1)}
for _ in range(M):
    a,b,c = map(int, input().split())
    G[a].append((b,c))
def solve(start, graph):
    costs = [ float("inf") for _ in range(N+1)]
    costs[start] = 0
    heap  = [(0, start)]
    while heap:
        c, u = heappop(heap)
        for v,w in graph[u]:
            if costs[v] > c+w:
                costs[v] = c+w
                heappush(heap, (costs[v],v))
                
    costs = [0 if c == float("inf") else c for c in costs]
    return costs
for i in range(1, N+1):
    print(*solve(i, G)[1:])