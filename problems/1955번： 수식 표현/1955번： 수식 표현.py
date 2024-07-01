#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1955                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1955                          #+#        #+#      #+#     #
#     Solved: 2024-06-18 11:45:07 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

INF = float("inf")
N = int(input())
dp = [INF] * (N + 1)
 
fcts = [1] * 9
for i in range(1, 9):
    fcts[i] = fcts[i-1]*i
dp[1] =1 
 
for i in range(2,N+1):
    ret = i 
    for j in range(1,i//2+1):
        ret = min(ret, dp[j] + dp[i-j])
    for j in range(2, int(i**0.5)+1):
        if not i%j:
            ret= min(ret, dp[j]+dp[i//j])
    for j in range(2,9):
        if i == fcts[j]:
            ret = min(ret, dp[j])
    dp[i] = ret 
 
print(dp[N])