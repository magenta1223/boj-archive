#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 13907                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/13907                         #+#        #+#      #+#     #
#     Solved: 2024-07-26 00:10:10 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

# 통행료의 합이 가장 적은 경로로 이동 = 다익스트라 + dp 
# 양방향 도로, 통행료가 존재
# 세금이 K번 오르고, i번째 인상 시, TAXES_i만큼 모든 도로의 세금이 오른다 


# S->D 경로가
# 1. 도로 개수는 1개, 비용은 1000 
# 2. 도로 개수는 100개, 비용은 901 
# 여기서 최소 비용은 2번도로지만 
# 1원이라도 인상 시 1번이 더 작은 비용이 된다. 
# 즉, 도로 개수와 비용 모두 카운트를 해놓고 그 중 최솟값을 계속 리턴하면 됨 

# 도시가 최대 1000개 -> 임의의 도시에 이르는 도로의 개수는 최대 999개 



from heapq import heappop, heappush 
INF = float("inf")
input = open(0).readline 

N,M,K = map(int,input().split())
S,D =  map(int,input().split())
G = {i : [] for i in range(1,N+1)}
for _ in range(M):
    a,b,w =  map(int,input().split())
    G[a].append((b,w))
    G[b].append((a,w))

TAXES = [int(input()) for _ in range(K)]

def dijkstra(dprt, dest):
    
    # 세금 인상 시 최소비용을 알기 위해 사용 도로 갯수별 비용을 알아야 함 
    costs = [[INF] * (N+1) for _ in range(N+1)]
    costs[dprt][0] = 0 
    heap = [(0,0,dprt)] # cost, nroads, node 
    
    # 세금은 도로1개마다 동일하게 상승 
    # = 도로 개수가 많을수록 불리 
    # 어떤 도시에
    # 1) 도로 i개를 사용해 방문가능한 최소비용들이 존재
    # 2) 그 중 최소 비용이 존재 
    # 전체 최소비용보다 도로를 많이 사용하면 -> 세금 인상시 최소비용보다 불리, 탐색할 필요가 없음. 


    optimalPath_roadCnt = [N] * (N+1)
    optimalPath_roadCnt[dprt] = 0 
    while heap:
        curCost, curRoad, curNode = heappop(heap)
        if curCost > costs[curNode][curRoad] or curRoad > optimalPath_roadCnt[curNode]:
            continue 
        
        for nextNode, w in G[curNode]:
            nextRoad = curRoad+1 
            nextCost = curCost+w 
            
            if costs[nextNode][nextRoad] <= nextCost:
                continue 

            costs[nextNode][nextRoad] = nextCost
            if costs[nextNode][optimalPath_roadCnt[nextNode]] > nextCost:
                optimalPath_roadCnt[nextNode] = nextRoad

            if nextRoad <= optimalPath_roadCnt[nextNode]:
                heappush(heap, (nextCost, nextRoad, nextNode))
    return costs[dest]

cost = dijkstra(S,D)
print(min(cost))
t = 0
for i in range(K):
    t += TAXES[i]
    print(min([cost[j] + j*t for j in range(N)])) # 




