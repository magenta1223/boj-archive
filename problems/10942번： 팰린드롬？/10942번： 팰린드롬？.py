#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 10942                            :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/10942                         #+#        #+#      #+#     #
#     Solved: 2024-02-28 11:43:16 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

input = open(0).readline
N=int(input())
L=[0] + list(map(int,input().split()))
M=int(input())
 
dp = [[0] * (N+1) for _ in range(N+1)]
# 자기자신은 항상 팰린드롬
for i in range(N+1):
    dp[i][i] = 1
# 인접한 2개가 같다면 팰린드롬
for i in range(N):
    if L[i] == L[i+1]:
        dp[i][i+1] = 1
# 3개 이상부터는
# dp[i][j] =  if dp[i+1][j-1] and L[i] == L[j] 
# 길이를 짧은것부터 늘려가면서 
# l=S와 E의 index 차이 -> 최대 N-1 
for l in range(2,N):
    for i in range(1, N-l+1):
        j = i+l
        if L[i] == L[j] and dp[i+1][j-1]:
            dp[i][j] = 1
for _ in range(M):
    S,E = map(int, input().split())
    print(dp[S][E])