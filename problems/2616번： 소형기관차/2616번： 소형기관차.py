#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 2616                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/2616                          #+#        #+#      #+#     #
#     Solved: 2024-05-29 17:14:00 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N = int(input())
A = list(map(int, input().split()))
MAX = int(input())
dp = [[-1] * N for _ in range(3)]
 
cumsum = [0] * (N+1)
for i in range(1,N+1):
    cumsum[i] = cumsum[i-1] + A[i-1]
 
def get(a,b):
    return 0 if a > b else cumsum[min(b, N)] - cumsum[a]
 
dp = [[-1] * N for _ in range(3)]
dp[0][0] = cumsum[MAX]
for i in range(1,N):        
    dp[0][i] = max(dp[0][i-1], get(i,i+MAX))
 
for round in range(1,3):
    for i in range(MAX*round,N):
        dp[round][i] = max(dp[round][i-1], dp[round-1][i-MAX]+ get(i,i+MAX))
print(dp[-1][-1])