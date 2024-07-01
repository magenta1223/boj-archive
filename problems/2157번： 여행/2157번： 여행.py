#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2157                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2157                          #+#        #+#      #+#     #
#     Solved: 2024-03-18 16:06:33 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from collections import deque 
input = open(0).readline
N,M,K = map(int,input().split())
G = {i:[] for i in range(1,N+1)}
for _ in range(K):
    a,b,c = map(int,input().split())
    if a<b:
        G[a].append((b,c))
queue = deque([(1,1)])
dp = [[0] * (M+1) for _ in range(N+1)] # N번 도시를 M개를 거쳐 지날 때의 최대 편익 
while queue:
    a,n = queue.popleft()
    for b,c in G[a]:
        if n<M and dp[b][n+1] < dp[a][n] + c:
            dp[b][n+1] = dp[a][n] + c 
            queue.append((b,n+1))
print(max(dp[-1]))