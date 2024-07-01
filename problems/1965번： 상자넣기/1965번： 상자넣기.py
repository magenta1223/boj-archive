#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1965                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1965                          #+#        #+#      #+#     #
#     Solved: 2024-03-18 14:10:37 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N = int(input())
L = list(map(int,input().split()))
 
dp = [1] * (N)
for i in range(N):
    for j in range(i):
        if L[j] < L[i]:
            dp[i] = max(dp[i], dp[j] + 1)
 
print(max(dp))