#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 14938                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/14938                         #+#        #+#      #+#     #
#     Solved: 2024-04-04 12:50:52 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from collections import deque 
INF = float("inf")
 
def bfs(start):
    q = deque([(start, 0)])
    visited = [INF] * (N+1)
    visited[start] = 0
    while q:
        x,d =q.popleft()
        for nx, _d in G[x]:
            nd = d+_d 
            if nd <= M and visited[nx] > nd:
                visited[nx] = nd  
                q.append((nx,nd))
    return sum([T[i] for i in range(1,N+1) if visited[i] != INF])
 
N,M,R = map(int,input().split())
T = [0] + list(map(int,input().split()))
G = {i : [] for i in range(1,N+1)}
for _ in range(R):
    a,b,l = map(int,input().split())
    G[a].append((b,l))
    G[b].append((a,l))
 
print(max([bfs(i) for i in range(1,N+1)]))