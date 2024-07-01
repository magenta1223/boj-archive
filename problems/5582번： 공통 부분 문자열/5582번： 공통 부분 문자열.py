#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 5582                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/5582                          #+#        #+#      #+#     #
#     Solved: 2024-03-13 18:37:57 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

A,B = input().strip(), input().strip()
N,M = len(A), len(B)
dp = [[0] * M for _ in range(N)]
 
for i in range(N):
    if A[i] == B[0]:
        dp[i][0] = 1
 
for i in range(M):
    if A[0] == B[i]:
        dp[0][i] = 1
 
ans = dp[-1][-1]
 
for i in range(1,N):
    for j in range(1,M):
        if A[i] == B[j]:
            dp[i][j] = dp[i-1][j-1] + 1 
            ans = max(dp[i][j], ans)
 
print(ans, sep = '\n')