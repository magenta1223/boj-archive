#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 13398                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/13398                         #+#        #+#      #+#     #
#     Solved: 2024-05-14 10:19:41 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

input = open(0).readline 
 
N = int(input())
A = list(map(int, input().split()))
INF = float("inf")
dp = [[-INF]*2 for _ in range(N)]
 
dp[0][0] = A[0]
dp[0][1] = 0 
 
for i in range(1,N):
    dp[i][0] = max(dp[i-1][0]+A[i], A[i])
    dp[i][1] = max([dp[i-1][0], dp[i-1][1]+A[i]])
 
ans = dp[0][0] # dp[0][1]은 아무것도 포함하지 않음 
for i in range(1,N):
    ans = max(ans, max(dp[i]))
 
print(ans)