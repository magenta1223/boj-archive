#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1086                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1086                          #+#        #+#      #+#     #
#     Solved: 2024-07-22 08:47:43 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


from math import gcd 
input = open(0).readline 
N = int(input())
A = [input().strip() for _ in range(N)]
K = int(input())

R = [[0] * K for _ in range(N)]
# 이전 나머지 k에 i번째 수를 이어붙일 때 다음 나머지 
for i in range(N):
    for k in range(K):
        a = (10**len(A[i]))%K 
        R[i][k] = (k * a + (int(A[i])%K))%K


dp = [[0] * K for _ in range(1<<N)]
dp[0][0] = 1 


for bitmask in range(1<<N):
    for i in range(N):
        if bitmask & (1<<i):
            continue 
        for k in range(K):
            dp[bitmask|(1<<i)][R[i][k]] += dp[bitmask][k]

p,q = dp[-1][0], sum(dp[-1])
_gcd = gcd(p,q)
print(f"{p//_gcd}/{q//_gcd}")