#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 3176                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/3176                          #+#        #+#      #+#     #
#     Solved: 2024-07-05 05:44:33 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


# LCA를 해서
# costs를 삭삭 구하면서
# 최대길이 최소길이를 찾으면 됨 

# 1. levels
# 2. parents 
# 3. costs 필요한데
# 4. 메모리가 256이면 .. 흠. 

from collections import deque 
from math import log2, ceil 

input = open(0).readline

INF = float("inf")
N=int(input())
G = {i : [] for i in range(1,N+1)}

for _ in range(N-1):
    a,b,c = map(int,input().split())
    G[a].append((b,c))
    G[b].append((a,c))


maxDepth = ceil(log2(N))+1

def init(graph):
    # 1번 노드를 루트로 시작
    # 내려가면서 level을 늘린다
    levels = [0] * (N+1)
    parents = [[0] * maxDepth for _ in range(N+1)]
    costs = [[0] * maxDepth for _ in range(N+1)]
    shortest = [[0] * maxDepth for _ in range(N+1)]
    longest = [[0] * maxDepth for _ in range(N+1)]

    node = 1 
    q = deque([(node, 1)])
    levels[node] = 1 
    while q:
        node, lv = q.popleft()
        for child, c in graph[node]:
            if not levels[child]:
                levels[child] = lv+1
                q.append((child, lv+1))
                parents[child][0] = node  
                costs[child][0] = c 
                shortest[child][0] = c 
                longest[child][0] = c 
    
    for d in range(1, maxDepth):
        for i in range(1,N+1):
            parents[i][d] = parents[parents[i][d-1]][d-1]

            costs[i][d] = costs[i][d-1] + costs[parents[i][d-1]][d-1]
            shortest[i][d] = min(shortest[i][d-1], shortest[parents[i][d-1]][d-1])
            longest[i][d] = max(longest[i][d-1], longest[parents[i][d-1]][d-1])


    return levels, parents, costs, shortest, longest

def LCA(a, b):
    s,l = INF, 0
    if levels[a] > levels[b]:
        a,b = b,a 
    # 레벨을 같도록 조정한다
    for i in range(maxDepth-1, -1,-1):
        if levels[a] <= levels[parents[b][i]]:
            s = min(s, shortest[b][i])
            l = max(l, longest[b][i])
            b = parents[b][i]

            # print("b=",b)
    # 레벨이 같고, 노드가 같다면 그냥 리턴 
    if a==b:
        return s,l

    # 노드가 다르다면 조상이 같을 때 까지 올려라 
    for i in range(maxDepth-1, -1,-1):
        if parents[a][i] != parents[b][i]:
            s = min(s, shortest[a][i], shortest[b][i])
            l = max(l, longest[a][i], longest[b][i])
            a = parents[a][i]
            b = parents[b][i]
    
    # 조상이 같아짐. 
    return min(s, shortest[a][0], shortest[b][0]), max(l, longest[a][0], longest[b][0])

levels, parents, costs, shortest, longest = init(G)
K=int(input())
for _ in range(K):
    d,e = map(int,input().split())
    print(*LCA(d,e))