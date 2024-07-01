#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2228                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2228                          #+#        #+#      #+#     #
#     Solved: 2024-03-18 11:15:02 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N,M = map(int, input().split())
L = [int(input()) for _ in range(N)]
INF = float("inf")
dp = [[[-INF] * 2 for _ in range(M+1)] for _ in range(N+1)]
 
 
on, off = 0, 1 
 
# i번째 수를 사용, 0개의 구간, i번째 수를 미사용 
for i in range(N+1):
    dp[i][0][off] = 0 
 
 
for i in range(1,N+1):
    for j in range(1,M+1):
        # dp[i][j][0] = max([ dp[i-1][j][0], dp[i-1][j-1][1]]) +L[i-1] 
        # dp[i][j][1] = max([ dp[i-1][j][1], dp[i-1][j-1][0]]) +L[i-1] 
 
        # dp[i][j][1] = max(dp[i-1][j])
        # dp[i][j][0] = max(dp[i-1][j])
 
        dp[i][j][off] = max(dp[i-1][j])
        dp[i][j][on] = max([ dp[i-1][j][on], dp[i-1][j-1][off]]) +L[i-1] 
        
        
print(max(dp[-1][-1]))
 