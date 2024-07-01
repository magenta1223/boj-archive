#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 21921                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/21921                         #+#        #+#      #+#     #
#     Solved: 2024-05-10 14:58:47 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N,X=map(int,input().split())
V = list(map(int,input().split()))
 
dp = [0] * N
dp[0] = V[0]
for i in range(1,X):
    dp[i] = dp[i-1] + V[i]
for i in range(X,N):
    dp[i] = dp[i-1] + V[i] - V[i-X]
ans = max(dp)
if ans:
    print(ans, dp.count(ans), sep ='\n')
else:
    print("SAD")