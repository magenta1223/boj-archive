#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1854                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1854                          #+#        #+#      #+#     #
#     Solved: 2024-07-31 05:24:37 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #



# 총 N개의 줄을 출력
# i번째 줄은 1번에 i로 가는 k번째 최단경로를 출력 

# 1. 최단경로를 구한다. 
# 2. 그것보다는 큰 최단경로를 구한다
# 3. k번 반복? 

from heapq import heappop, heappush
input = open(0).readline 
INF = float("inf")

N,M,K = map(int, input().split())
G = {i:[] for i in range(1,N+1)}
for _ in range(M):
    a,b,c = map(int, input().split())
    G[a].append((b,c))

def dijkstra():
    costs = [[] for _ in range(N+1)]
    q = [(0,1)]
    heappush(costs[1], 0)
    while q:
        curCost, cur = heappop(q)
        for next, c in G[cur]:
            nextCost = curCost+c
            if len(costs[next]) < K or -costs[next][0] > nextCost:
                heappush(costs[next], -nextCost)
                if len(costs[next]) > K:
                    heappop(costs[next])
                heappush(q, (nextCost, next))
    return costs

costs = dijkstra()

for i in range(1,N+1):
    print(-costs[i][0] if len(costs[i]) == K else -1)
