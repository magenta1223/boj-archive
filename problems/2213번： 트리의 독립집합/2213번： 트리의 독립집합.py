#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2213                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2213                          #+#        #+#      #+#     #
#     Solved: 2024-03-25 20:50:13 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N = int(input())
W = list(map(int,input().split()))
E = [list(map(int,input().split())) for _ in range(N-1)]
G = {i:[] for i in range(1,N+1)}
for a, b in E:
    G[a].append(b)
    G[b].append(a)
 
visited = [0] * (N+1)
dp = [[0,0,0] for _ in range(N+1)]
 
for i in range(N):
    dp[i+1][2] = W[i]
 
def dfs(x):
    visited[x] = 1 
    nxs = [dfs(nx) for nx in G[x] if not visited[nx]]
    dp[x][0] = sum([max(dp[nx]) for nx in nxs])
    dp[x][1] = sum([dp[nx][0] for nx in nxs]) + W[x-1]
    return x 
 
 
dfs(1)
 
visited = [0] * (N+1)
visited[1] = 1 
n = 1
from collections import deque 
q =  deque([(1,0)])
backtrack = []
while q:
    np = 0
    x,p = q.popleft()
    if not p:
        if dp[x][0] <= dp[x][1]:
            backtrack.append(x) 
            np = 1 
 
    for nx in G[x]:
        if not visited[nx]:
            visited[nx] = 1 
            q.append((nx, np))
 
print(max(dp[1]))
print(*sorted(backtrack))