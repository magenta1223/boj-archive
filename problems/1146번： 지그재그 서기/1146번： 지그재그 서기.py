#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#     Problem Number: 1146                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#     By: magenta1223 <boj.kr/u/magenta1223>         +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#     https://boj.kr/1146                          #+#        #+#      #+#     #
#     Solved: 2024-04-30 15:06:27 by magenta1223  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

MOD = 1_000_000
N = int(input())
dp = [[-1] * N for _ in range(N)]
 
def dfs(left, right):
    idx = N-left-right 
    if idx == N:
        return 1 
    if dp[left][right] != -1:
        return dp[left][right]
    dp[left][right] = 0
    if not right:
        return dp[left][right]
    
    for i in range(right):
        dp[left][right] += dfs(right-1-i, left+i)
 
    return dp[left][right] % MOD 
 
if N==1:
    print(1)
    exit(0)
 
ans = 0 
for i in range(N):
    ans += dfs(i, N-i-1) 
    ans += dfs(N-i-1, i) 
print(ans % MOD)