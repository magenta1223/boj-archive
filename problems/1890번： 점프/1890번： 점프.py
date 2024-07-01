#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1890                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1890                          #+#        #+#      #+#     #
#     Solved: 2024-03-15 14:40:35 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
 
dp = [[0] * N for _ in range(N)]
dp[0][0] = 1
 
for i in range(N):
    for j in range(N):    
        v = A[i][j]
        if not v:
            continue
        ni,nj = i+v, j+v 
        if ni<N:
            dp[ni][j] += dp[i][j]
        if nj<N:
            dp[i][nj] += dp[i][j]
 
print(dp[-1][-1])