#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1750                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1750                          #+#        #+#      #+#     #
#     Solved: 2024-03-28 18:09:26 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import math
MOD = 10000003
N = int(input())
S = [int(input()) for _ in range(N)]
ans = 0
maxS = max(S) + 1
dp = [0] * maxS
for i in range(N):
    for j in range(1, maxS):
        if dp[j]:
            dp[math.gcd(j, S[i])] += dp[j]
    dp[S[i]] += 1
print(dp[1] % MOD)