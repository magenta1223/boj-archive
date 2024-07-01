#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 15486                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/15486                         #+#        #+#      #+#     #
#     Solved: 2024-04-01 13:25:58 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

input = open(0).readline 
N = int(input())
# T,P = [list(row) for row in zip(*[list(map(int,input().split())) for _ in range(N)])]
A = [list(map(int,input().split())) for _ in range(N)]
dp = [0] * (N+1)
 
# 뒤부터 
for i in range(N-1, -1, -1):
    # i번째 의뢰를 수행 불가 -> 복사 
    t, p = A[i]
    if i + t > N:
        dp[i] = dp[i + 1] 
    else:
        # 수행 가능 -> 갱신 
        dp[i] = max(dp[i + 1], p + dp[i+t]) 
print(dp[0]) 