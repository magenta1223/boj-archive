#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1699                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1699                          #+#        #+#      #+#     #
#     Solved: 2024-05-03 12:13:08 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import math 
INF = float("inf")
N=int(input())
dp = [INF] * (N+1)
squares = []
for i in range(1, int(math.sqrt(N)) + 1):
    sq = i*i
    dp[sq] = 1 
    squares.append(sq)
for i in range(1,N+1):
    for j in squares:
        if j > i:
            break 
        if dp[i-j] != INF:
            dp[i] = min(dp[i], dp[j] + dp[i-j])
print(dp[-1])