#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2169                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2169                          #+#        #+#      #+#     #
#     Solved: 2024-05-09 16:09:57 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

input = open(0).readline
N,M = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(N)]
dp = [[False] * M for _ in range(N)]
 
dp[0][0] = A[0][0]
for i in range(1,M):
    dp[0][i] = dp[0][i-1] + A[0][i]
 
for i in range(1,N):
    L2R,R2L = [0] * M, [0] * M 
    
    L2R[0] = dp[i-1][0] + A[i][0]
    for j in range(1,M):
        L2R[j] = max([dp[i-1][j], L2R[j-1]]) +A[i][j] 
 
    R2L[-1] = dp[i-1][-1] + A[i][-1]
    for j in range(M-2,-1,-1):
        R2L[j] = max([dp[i-1][j], R2L[j+1]]) +A[i][j] 
 
    dp[i] = [max(l2r, r2l) for l2r, r2l in zip(L2R, R2L)]
 
print(dp[-1][-1])