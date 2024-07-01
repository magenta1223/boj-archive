#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 14501                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/14501                         #+#        #+#      #+#     #
#     Solved: 2024-02-11 20:46:44 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N=int(input().strip())
T, P = map(list, zip(*[list(map(int, input().split())) for _ in range(N)]))
 
# DP
# N일째 종료하는 상담의 최대치를 DP[i]에 저장 
# dp[-1]
# 갱신 로직
# i일 이전의 모든 날짜 j일에 대해
# j일의 상담 이후 i일의 상담이 가능 + dp[i]보다 크다면 갱신 
# j이후 i가 가능할 조건
# 1. j상담이 끝났는가 -> i와 j의 차이가 T[j] 이상인가 
# 2. i상담이 N일 전에 끝나는가 
# N일 종료 시 최대 이익을 저장 
dp = [0] * N
for i in range(N):    
    if T[i]+i<=N:
        dp[i] = P[i]    
    for j in range(i+1):        
        if T[j] <= i-j and T[i]+i<=N:
            dp[i] = max(dp[i], dp[j] + P[i])
print(max(dp))