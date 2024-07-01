#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1516                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1516                          #+#        #+#      #+#     #
#     Solved: 2024-05-28 11:23:07 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from heapq import heappop, heappush
 
INF = float("inf")
N=int(input())
 
G = {i : [] for i in range(1,N+1)}
G[-1] = []
prereq = {i : [] for i in range(1,N+1)}
prereq[-1] = []
B = [-1] * (N+1)
COSTS = [INF] * (N+1)
heap = [(0,-1)]
for i in range(1,N+1):
    X = list(map(int,input().split()))
    B[i] = X[0] 
    if len(X) == 2:
        G[-1].append(i) 
    else:
        prereq[i].extend(X[1:-1])
        for x in X[1:-1]:
            G[x].append(i)
 
while heap:
    cur_cost, now = heappop(heap)
    if COSTS[now] < cur_cost:
        continue 
    for next in G[now]:
        _c = max([COSTS[i] for i in prereq[next]]) if prereq[next] else 0
        next_cost = _c + B[next]
        # print(f"{now} -> {next} 현재비용: {cur_cost}, 빌드타임: {B[next]} 선행조건: {_c} 총합: {next_cost}")
        # 도달 하는 비용이 싸면서 + 선행조건이 전부 클리어되어야 함. 
        if COSTS[next] > next_cost:
            COSTS[next] = next_cost
            heappush(heap, (next_cost, next))
        # else:
        #     if not all([COSTS[i] != INF for i in prereq[now]]):
        #         print("선행조건 미달", [i for i in prereq[now] if COSTS[i] == INF])
        #     else:
        #         print("비용이 더 높음", COSTS[next])
 
print(*COSTS[1:], sep = '\n')