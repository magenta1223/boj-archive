#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 31938                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/31938                         #+#        #+#      #+#     #
#     Solved: 2024-07-11 04:08:13 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #



# 1번에서 출발
# 2~N에 도착

# 여러 트럭이 동시에 진행하는 경우에는 뒤따르는 트럭의 운송비가 10% 절감된다
# = 같이 이동하는 길이를 최대한 늘려야 한다. 
# 최단 거리 루트가 여러개일 때
# 1. 거기 도착하는 인접 노드를 전부 보고
# 2. 그 비용이 가장 큰 노드로 ㄱㄱ. 그만큼 아낄 수 있다. 

from heapq import heappop, heappush 

INF = float("inf")

input = open(0).readline
def daijkstra():
    heap = [(0,1)]
    costs = [INF] * (N+1)
    prevs = [[] for _ in range(N+1)]
    costs[1] = 0
    while heap:
        curCost, now = heappop(heap)
        if curCost > costs[now]:
            continue 
        for next, w in G[now]:
            nextCost = curCost + w 
            if costs[next] > nextCost:
                costs[next] = nextCost 
                prevs[next] = [now]
                heappush(heap, (nextCost, next))
            elif costs[next] == nextCost:
                prevs[next].append(now)
    return costs, prevs 

N,M = map(int,input().split())
G = {i:[] for i in range(1,N+1)}
for i in range(M):
    a,b,c = map(int,input().split())
    G[a].append((b,c))
    G[b].append((a,c))

costs, prevs = daijkstra()

ans = 0
for i in range(2,N+1):
    d = costs[i]
    d_prev = max([costs[prev] for prev in prevs[i]])
    ans += d-d_prev + (d_prev//10)*9 
print(ans)