#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1939                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1939                          #+#        #+#      #+#     #
#     Solved: 2024-07-09 02:11:41 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


# X-> Y 한 번의 이동에서 옮길 수 있는 최대 무게 
# X->Y에 해당하는 모든 경로를 찾고
# 경로가 감당하는 최대무게 = 경로에 속한 도로의 w의 최솟값 
# 의 최댓값을 구하세요 
# 이분탐색 


from heapq import heappop, heappush 

INF = float("inf")
input = open(0).readline 
N,M = map(int, input().split())

G = {i : [] for i in range(1,N+1)}
for _ in range(M):
    a,b,c = map(int,input().split())
    G[a].append((b,c))
    G[b].append((a,c))


def solve(threshold):
    # threshold 이상으로 최단 경로 
    costs = [INF] * (N+1)
    costs[X] = 0 
    heap = [(0, X)]
    while heap:
        curCost, now = heappop(heap)
        for next, c in G[now]:
            if c < threshold:
                continue 
            nextCost = curCost + c 
            if costs[next] > nextCost:
                costs[next] = nextCost 
                heappush(heap, (nextCost, next))
    return costs[Y] != INF
    
X,Y = map(int,input().split())
s,e = 0, 1_000_000_001 


# 
while s<=e:
    mid = (s+e)//2
    if solve(mid):
        s = mid+1 
    else:
        e = mid-1  
print(e)