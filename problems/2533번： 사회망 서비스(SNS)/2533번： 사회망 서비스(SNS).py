#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2533                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2533                          #+#        #+#      #+#     #
#     Solved: 2024-04-12 13:05:07 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys 
sys.setrecursionlimit(10**6)
 
def dfs(x):
    visited[x] = True 
    for nx in G[x]:
        if not visited[nx]:
            dfs(nx)
            dp[x][0] += min(dp[nx])
            dp[x][1] += dp[nx][0]
 
input = open(0).readline 
N = int(input())
G = {i : [] for i in range(1,N+1)}
for _ in range(N-1):
    a,b = map(int,input().split())
    G[a].append(b)
    G[b].append(a)
 
dp = [[1,0] for _ in range(N+1)] 
visited = [False] * (N+1)
dfs(1)
print(min(dp[1]))