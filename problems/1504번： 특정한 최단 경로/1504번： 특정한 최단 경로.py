#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1504                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1504                          #+#        #+#      #+#     #
#     Solved: 2024-01-29 16:30:43 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N,E=map(int, input().split())
G={ i : [] for i in range(1,N+1)}
for _ in range(E):
    u, v, w = map(int, input().split())
    G[u].append((v, w))
    G[v].append((u, w))
 
import heapq
def solve(start, end):
    costs = [float("inf") for _ in range(N+1)]
    costs[start] = 0
    heap = [(0, start)]
    while heap:
        cur_cost, cur_node = heapq.heappop(heap)
        if cur_cost > costs[cur_node]: # 탐색 필요 x
            continue
        for v, w in G[cur_node]:
            if costs[v] > cur_cost + w:
                costs[v] = cur_cost + w
                heapq.heappush(heap, (costs[v], v))
    return costs[end]
    
V1, V2 = map(int, input().split())
l=[1, V1, V2, N]
c1 = 0
for i in range(3):
    sub_cost = solve(l[i], l[i+1])
    c1+=sub_cost
l=[1, V2, V1, N]
c2 = 0
for i in range(3):
    sub_cost = solve(l[i], l[i+1])
    c2+=sub_cost
print( -1 if min(c1, c2) == float("inf") else min(c1, c2))