#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 22954                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/22954                         #+#        #+#      #+#     #
#     Solved: 2024-05-17 17:20:12 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

input = open(0).readline 
 
N,M = map(int,input().split())
G = {i : [] for i in range(1,N+1)}
EDGES = []
for i in range(1,M+1):
    u,v = map(int,input().split())
    G[u].append((i,v))
    G[v].append((i,u))
    EDGES.append((i,u,v))
 
# 서로 다른 크기의 트리로 분할 -> N<=2에서는 불가능 
if N<=2 or M <= N-3:
    print(-1)
    exit(0)
 
def dfs(root):
    q, n_list, e_list = [root], [root], []
    visited[root] = True 
    while q: 
        now = q.pop()
        for idx, next in G[now]:
            if not visited[next]:
                visited[next] = True 
                e_list.append(idx)
                n_list.append(next)
                q.append(next)
 
    return e_list, n_list, now
 
 
visited = [False]*(N+1)
edges, nodes, leafs = [],[],[]
for i in range(1, N+1):
    if not visited[i]:
        _edges, _nodes, _leaf = dfs(i)
        edges.append(_edges)
        nodes.append(_nodes)
        leafs.append(_leaf)
 
if len(nodes) > 2:
   print(-1)
   exit(0)
elif len(nodes) == 2:
    N1,N2 = len(nodes[0]), len(nodes[1])
    if N1 == N2:
       print(-1)
       exit(0)
    print(N1,N2)
    for i in range(2):
       print(*nodes[i])
       print(*edges[i])
    exit(0)
 
# 1개면 분할해야됨. 
edges, nodes, leaf = edges[0], nodes[0], leafs[0]
nodes.remove(leaf)
 
edges_A = list()
for idx in edges :
    _, a, b = EDGES[idx-1]
    if a == leaf or b == leaf:
        continue
    edges_A.append(idx)
 
print(N-1, 1)
print(*nodes)
print(*edges_A)
print(leaf)
print()