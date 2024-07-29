#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 17831                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/17831                         #+#        #+#      #+#     #
#     Solved: 2024-07-29 01:06:15 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys 
input = open(0).readline 

N = int(input())
P = [0, 0] + list(map(int, input().split()))
A = [0] + list(map(int,input().split()))

sys.setrecursionlimit(N+100)

G = {i : [] for i in range(1,N+1)}
for i in range(2,N+1):
    G[P[i]].append(i)

dp = [[0, 0]  for _ in range(N+1)]

def dfs(node):
    noSyn = 0 
    for next in G[node]:
        dfs(next)
        noSyn += max(dp[next])
    
    # 자식노드와 시너지 x 
    dp[node][0] = noSyn 
    
    # 시너지 계산 
    Syn = 0
    for next in G[node]:
        Syn = max(Syn, noSyn - max(dp[next]) + dp[next][0] + A[node]*A[next])        
    dp[node][1] = Syn     
dfs(1)
print(max(dp[1]))




"""
3
1 1 
1 2 3 

ans: 3 
"""