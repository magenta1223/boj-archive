#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1256                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1256                          #+#        #+#      #+#     #
#     Solved: 2024-05-03 14:35:24 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N,M,K = map(int,input().split())
 
dp = [[0] * (M+1) for _ in range(N+1)]
dp[0] = [1] * (M+1)
for i in range(N+1):
    dp[i][0] = 1 
 
for i in range(1,N+1):
    for j in range(1,M+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]
 
if K > dp[-1][-1]:
    print(-1)
    exit(0)
 
ans = ""
while K and N and M:
    v = dp[N][M] * N // (N+M)
    if K > v:
        ans += "z"
        M -= 1 
        K -= v 
    else:
        ans += "a"
        N -= 1 
print(ans+"a"*N if N else ans+"z"*M)