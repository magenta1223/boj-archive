#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 17472                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/17472                         #+#        #+#      #+#     #
#     Solved: 2024-06-12 14:55:33 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from collections import deque 
D = [(-1,0), (0,1), (1,0), (0,-1)]
N,M = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(N)]
visited = [[False] *M for _ in range(N)]
 
def bfs(x,y):
    q = deque([(x,y)])
    island = [(x,y)]
    visited[x][y] = True 
    while q:
        x,y = q.popleft()
        for dx, dy in D:
            nx,ny = x+dx, y+dy 
            if 0<=nx<N and 0<=ny<M and not visited[nx][ny] and A[nx][ny]:
                visited[nx][ny] = True 
                q.append((nx,ny))
                island.append((nx,ny))
 
    return island 
 
n_island = 0 
islands = []
for i in range(N):
    for j in range(M):
        if visited[i][j] or not A[i][j]:
            continue 
        islands.append(bfs(i,j))
        n_island += 1 
 
# 연결 가능한 섬 찾기 
def find_connectable(island_idx):
    # 연결 가능한 섬 찾기.
    # 1. 두 섬 사이에는 다른 섬이 없어야 함. 
    # 2. 각 셀을 직선으로 연결 
    for x1,y1 in islands[island_idx]:
        for j in range(n_island):
            if j == island_idx:
                continue 
            for x2,y2 in islands[j]:
                # 직선으로 연결가능?
                mx1, mx2 = min(x1, x2), max(x1, x2)
                my1, my2 = min(y1, y2), max(y1, y2)
 
                if x1 == x2 and my2-my1>2 and not sum([A[x1][i] for i in range(my1+1, my2)]):
                    edges.append((my2-my1-1, island_idx,j))
 
                if y1 == y2 and mx2-mx1>2 and not sum([A[i][y1] for i in range(mx1+1, mx2)]):
                    edges.append((mx2-mx1-1, island_idx,j))
                
 
edges = []
for i in range(n_island):
    find_connectable(i)
 
edges.sort(key=lambda x:x[0])
 
# 크루스칼 
parent = [i for i in range(n_island)]
def find(a):
    if a == parent[a]:
        return a 
    parent[a] = find(parent[a])
    return parent[a]
 
ans = 0 
for i in range(len(edges)):
    c, a, b = edges[i]
    a,b = find(a), find(b)
    if a != b:
        parent[a] = parent[b]
        ans += c 
    else:
        # 같은데 연결하면 사이클임 
        pass 
 
for i in range(n_island):
    find(i)
 
print(ans if len(set(parent)) == 1 else -1)