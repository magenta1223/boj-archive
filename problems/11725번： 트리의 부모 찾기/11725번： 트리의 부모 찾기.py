#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 11725                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/11725                         #+#        #+#      #+#     #
#     Solved: 2024-03-29 23:57:20 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys 
sys.setrecursionlimit(10**5)
 
input = open(0).readline 
 
 
N = int(input())
G = {i : [] for i in range(1,N+1)}
for _ in range(N-1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)
 
parent = [0] * (N+1)
visited = [False] * (N+1)
def dfs(node):
    for next in G[node]:
        if not visited[next]:
            visited[next] = True 
            parent[next] = node 
            dfs(next)
visited[1] = True
dfs(1)
print(*parent[2:], sep ='\n')