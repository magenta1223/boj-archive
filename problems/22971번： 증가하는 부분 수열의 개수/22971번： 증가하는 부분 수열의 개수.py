#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 22971                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/22971                         #+#        #+#      #+#     #
#     Solved: 2024-07-19 03:07:43 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #



MOD = 998_244_353
N = int(input())
A = list(map(int,input().split()))

# i where 0<=i<N 에 대해 A[i]에서 종료하는 LIS의 개수 출력 
dp = [1] * N 
for i in range(1,N):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] += dp[j]
    dp[i] %= MOD

print(*dp)