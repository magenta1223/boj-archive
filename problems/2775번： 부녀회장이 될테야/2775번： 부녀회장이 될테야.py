#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2775                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2775                          #+#        #+#      #+#     #
#     Solved: 2024-05-03 11:25:47 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

dp = [[0] * 15 for _ in range(15)]
dp[0] = [i for i in range(15)]
 
for k in range(1,15):
    for n in range(1,15):
        dp[k][n] = dp[k][n-1] + dp[k-1][n]
 
 
for _ in range(int(input())):
    k,n = int(input()), int(input())
    print(dp[k][n])
 