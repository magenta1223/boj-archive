#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 9655                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/9655                          #+#        #+#      #+#     #
#     Solved: 2024-05-03 12:41:14 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N=int(input())
dp = [0] * (max(4,N)+1)
dp[1] = 1
dp[2] = 2 
dp[3] = 1 
for i in range(4,max(4,N)+1):
    dp[i] = min(dp[i-1] + 1, dp[i-3] + 1)
print("SK" if dp[N] % 2 else "CY")