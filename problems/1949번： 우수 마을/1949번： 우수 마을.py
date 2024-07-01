#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1949                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1949                          #+#        #+#      #+#     #
#     Solved: 2024-03-19 10:23:48 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys 
sys.setrecursionlimit(10**5)
 
N = int(input())
V = [0] + list(map(int,input().split()))
G = {i : [] for i in range(1,N+1)}
for _ in range(N-1):
    a,b = map(int,input().split())
    G[a].append(b)
    G[b].append(a)
 
visited = [0 for _ in range(N+1)]
 
def dfs(x):
    visited[x] = 1 
    for nx in G[x]:
        if not visited[nx]:
            dfs(nx)
            dp[x][1] += dp[nx][0]
            dp[x][0] += max(dp[nx])
 
dp = [[0, V[i]] for i in range(N+1)] 
dfs(1)
print(max(dp[1][1], dp[1][0]))
 