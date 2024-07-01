#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1761                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1761                          #+#        #+#      #+#     #
#     Solved: 2024-05-22 17:40:04 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from math import ceil, log2 
 
input = open(0).readline 
 
N =int(input())
G = {i : [] for i in range(1,N+1)}
for _ in range(N-1):
    a,b,c = map(int,input().split())
    G[a].append((b,c))
    G[b].append((a,c))
 
 
MAX_DEPTH = ceil(log2(N))+1
 
 
def init():
    parents = [[0] * MAX_DEPTH for _ in range(N+1)]
 
    costs = [[0] * MAX_DEPTH for _ in range(N+1)]
 
    levels = [0] * (N+1)
    levels[1] = 1
    nodes = [(1,1)]
    while nodes:
        now, level = nodes.pop()
        for next, cost in G[now]: 
            if not levels[next]:
                levels[next] = level+1
                nodes.append((next, level+1))
                parents[next][0] = now 
                costs[next][0] = cost
 
    # 2의 배수로 거슬러 올라가면서 parents와 costs를 업데이트 
    for d in range(1,MAX_DEPTH):
        for i in range(1,N+1):
            parents[i][d] = parents[parents[i][d-1]][d-1]
            costs[i][d] = costs[parents[i][d-1]][d-1] + costs[i][d-1]
 
 
    return parents, costs, levels
 
def find_LCA(a,b):
    total_cost = 0
    # 1. level을 맞추면서 비용 계산 
    if levels[a] < levels[b]:
        a,b = b,a
 
    # a의 level을 b까지 올리기 
    for d in range(MAX_DEPTH-1,-1,-1):
        # level 이 다르면 
        if levels[a] - levels[b] >= 2**d :
            total_cost += costs[a][d]
            a = parents[a][d]
            
 
    # 2. 같은 노드라면 -> 끝 
    if a==b:
        return total_cost
    
    # 3. 다르다면 함께 올리면 됨 
    for d in range(MAX_DEPTH-1,-1,-1):
        # 조상이 달라지면 -> 올려올려!!! 
        if parents[a][d] != parents[b][d]:
            total_cost += costs[a][d] + costs[b][d]
            a = parents[a][d]
            b = parents[b][d]
 
    if a==b:
        return total_cost
    
    return total_cost + costs[a][0] + costs[b][0]
 
 
 
parents, costs, levels = init()
 
M =int(input())
for _ in range(M):
    a,b = map(int,input().split())
    print(find_LCA(a,b))