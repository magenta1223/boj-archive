#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2294                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2294                          #+#        #+#      #+#     #
#     Solved: 2024-03-13 18:10:39 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N,K = map(int, input().split())
C = [int(input()) for _ in range(N)]
C = list(set(C))
INF = float("inf")
dp = [INF for _ in range(K+1)]
dp[0] = 0
 
for c in C:
    for k in range(c, K+1):
        dp[k] = min(dp[k-c] + 1, dp[k])
print(dp[-1] if dp[-1] != INF else -1)