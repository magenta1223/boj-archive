#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 17626                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/17626                         #+#        #+#      #+#     #
#     Solved: 2024-03-29 19:27:26 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from math import sqrt 
 
N = int(input())
dp = [5] * (N+1)
 
for i in range(int(sqrt(N)) + 1):
    dp[i*i] = 1
 
for i in range(1,N+1):
    if dp[i] == 1:
        continue
    for j in range(1, int(sqrt(i))+1):
        dp[i] = min(dp[i], dp[i-j*j] + 1)
print(dp[-1])