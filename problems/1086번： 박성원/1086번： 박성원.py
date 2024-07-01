#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1086                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1086                          #+#        #+#      #+#     #
#     Solved: 2024-02-28 21:47:18 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from math import gcd 
input = open(0).readline 
N=int(input().strip())
L=[int(input().strip()) for _ in range(N)]
K=int(input().strip())
 
next_remainders = [[0] * K for _ in range(N)]
for i in range(N):
    for j in range(K):
        a=(10**len(str(L[i]))) % K
        next_remainders[i][j] = (j * a + (L[i] % K)) % K
        
# dp[i][j] : i -> bitmask, j -> 나머지 
dp = [[0] * K for _ in range(1<<N)]
dp[0][0] = 1 # 아무런 수도 사용하지 않고 나머지 0인 방법은 1가지 존재 
 
# 모든 조합에 대해 순차적으로 
for i in range(1<<N):
    # j번째 수를 추가할건데 
    for j in range(N):
        # 현재 조합 i에 j가 포함되면 안됨. 
        if i & (1 << j): 
            continue
        for k in range(K):
            # i번째 조합에 나머지 k인 수에 j번째 수를 추가할 경우, 다음 나머지 
            next_remainder = next_remainders[j][k]
            dp[i|(1<<j)][next_remainder] += dp[i][k] # 현재 가능한 방법 수를 추가 
 
a,b=dp[-1][0], sum(dp[-1])
g = gcd(a,b)
print(f"{a//g}/{b//g}")