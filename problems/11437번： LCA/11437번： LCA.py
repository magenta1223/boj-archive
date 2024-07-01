#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 11437                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/11437                         #+#        #+#      #+#     #
#     Solved: 2024-02-28 15:01:20 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from collections import deque 
input = open(0).readline
# naive 
# def find_lca(a,b):
#     while a != b:
#         la, lb = levels[a], levels[b]
#         if la >= lb:
#             a = parent[a]
#         if la <= lb:
#             b = parent[b] 
#     return a 
 
def find_lca(a,b):
    while a != b:
        la, lb = levels[a], levels[b]
        if la >= lb:
            a = parent[a]
        if la <= lb:
            b = parent[b] 
    return a 
 
 
N = int(input())
G = {i:[] for i in range(1,N+1)}
for _ in range(N-1):
    a,b = map(int,input().split())
    G[a].append(b)
    G[b].append(a)
 
queue = deque([(1, 1)])
levels = [False] * (N+1)
parent = [False] * (N+1)
levels[1] = 1
parent[1] = 0
 
while queue:
    node, level = queue.popleft()
    next_level = level+1
    for next_node in G[node]:
        if not levels[next_node]:
            levels[next_node] = next_level
            parent[next_node] = node
            queue.append((next_node, next_level))
 
# parent를 2차원 배열 -> parent[x][k] = x번 정점의 2^k번째 조상 노드의 번호
# 를 어떻게 배열 하나요.. 
 
 
 
M = int(input())
for _ in range(M):
    a,b = map(int,input().split())    
    print(find_lca(a,b))