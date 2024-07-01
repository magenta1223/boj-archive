#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 14517                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/14517                         #+#        #+#      #+#     #
#     Solved: 2024-05-22 16:45:31 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys 
sys.setrecursionlimit(10**4)
 
MOD = 10007 
 
S = input().strip()
N = len(S)
 
dp = [[0] * N for _ in range(N)]
for i in range(N):
    dp[i][i] = 1 
 
for i in range(N-1):
    if S[i] == S[i+1]:
        dp[i][i+1] = 3 # i~i, i+1~i+1, i~i+1
    else:
        dp[i][i+1] = 2
 
 
for l in range(2,N):
    for i in range(N-l):
        j = i+l
        dp[i][j] = (dp[i+1][j] + dp[i][j-1] + (1 if S[i] == S[j] else - dp[i+1][j-1])) % MOD
 
# print(*dp, sep = '\n')
print(dp[0][-1])