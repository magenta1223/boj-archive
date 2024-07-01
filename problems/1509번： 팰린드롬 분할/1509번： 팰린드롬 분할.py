#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1509                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1509                          #+#        #+#      #+#     #
#     Solved: 2024-03-05 15:24:13 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

S = list(input().strip())
N = len(S)
dp = [[False] * N for _ in range(N)] # 
for i in range(N):
    dp[i][i] = True 
for i in range(N-1):
    if S[i] == S[i+1]:
        dp[i][i+1] = True 
        
for l in range(2, N):
    for i in range(N-l):
        dp[i][i+l] = True if dp[i+1][i+l-1] and S[i] == S[i+l] else False 
 
dp2 = [float("inf")] * (N+1)
dp2[0] = 0 #
dp2[1] = 1 
for i in range(2, N+1):
    for j in range(i):
        # j+1번째 문자 ~ i번째 문자를 팰린드롬으로 만들 수 있는지 
        if dp[j][i-1] and dp2[i] > dp2[j] + 1: 
            dp2[i] = dp2[j]+1            
print(dp2[-1])