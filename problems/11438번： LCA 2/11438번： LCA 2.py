#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 11438                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/11438                         #+#        #+#      #+#     #
#     Solved: 2024-02-28 16:13:17 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from collections import deque 
 
input = open(0).readline
 
N = int(input())
max_depth = 21 # N+1
G = {i:[] for i in range(1,N+1)}
for _ in range(N-1):
    a,b = map(int,input().split())
    G[a].append(b)
    G[b].append(a)
 
queue = deque([(1, 1)])
levels = [False] * (N+1)
parent = [[0] * max_depth for _ in range(N+1)]
levels[1] = 1
 
def find_lca(a,b):
    la, lb = levels[a], levels[b]
    a,b,la,lb = (a,b,la,lb) if la > lb else (b,a,lb,la)
 
    for i in range(max_depth, -1, -1):
        if levels[a] - levels[b] >= 2**i:
            a = parent[a][i]
    
    if a == b:
        return a
    for i in range(max_depth-1,-1,-1):
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]
    
    return parent[a][0]
 
while queue:
    node, level = queue.popleft()
    next_level = level+1
    next_nodes = G[node]
    for next_node in G[node]:
        if not levels[next_node]:
            levels[next_node] = next_level
            parent[next_node][0] = node
            queue.append((next_node, next_level))
            
for depth in range(1,max_depth):
    for x in range(1,N+1):
        parent[x][depth] = parent[parent[x][depth-1]][depth-1]
 
M = int(input())
for _ in range(M):
    a,b = map(int,input().split())    
    print(find_lca(a,b))