#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2092                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2092                          #+#        #+#      #+#     #
#     Solved: 2024-03-28 15:42:37 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from collections import Counter 
MOD = 1_000_000 
 
T,A,S,B = map(int,input().split())
L = list(map(int,input().split()))
C = {i : 0 for i in range(1,T+1)}
C.update(dict(Counter(L)))
 
total = 0
dp = [[0 for _ in range(A+1)] for _ in range(T+1)]
# i번째 숫자를 j개 사용 
 
 
for i in range(1,T+1):
    for k in range(C[i]+1): # i번째 숫자를 k번 사용
        dp[i][k] += 1
 
    for j in range(1,A+1):
        dp[i][j] += dp[i-1][j] # i번째 사용안하고 i-1까지 총 j개 사용
        for k in range(1,C[i]+1):
            if j-k >0:
                dp[i][j] += dp[i-1][j-k] # i를 k개 사용
                dp[i][j] %= MOD
 
 
for i in range(S,B+1): # t까지 s부터 b 개수만큼 사용한 개수 합 구하기
    total += dp[T][i]%MOD
print(total%MOD)