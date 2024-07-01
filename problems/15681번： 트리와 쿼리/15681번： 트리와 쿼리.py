#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 15681                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/15681                         #+#        #+#      #+#     #
#     Solved: 2024-04-12 12:18:14 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys 
sys.setrecursionlimit(10**5)
def dfs(x):
    dp[x] = 1
    for nx in G[x]:
        if dp[nx] == -1:
            dp[x] += dfs(nx)
    return dp[x]
input = open(0).readline 
N,R,Q = map(int,input().split())
G = {i : [] for i in range(1,N+1)}
for _ in range(N-1):
    a, b = map(int,input().split())
    G[a].append(b)
    G[b].append(a)
dp = [-1] * (N+1)
dfs(R)
for _ in range(Q):
    print(dp[int(input())])